import torch
from torchvision import models, transforms
from PIL import Image

# Загружаем предобученную модель
model = models.resnet50(pretrained=True)
model.eval()

# Сопоставление классов (предположим, что мы используем стандартный ImageNet)
with open("classification/imagenet_classes.txt") as f:
    labels = [line.strip() for line in f]

# Функция классификации
def classify(image_path):
    # Подготовка изображения
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img = Image.open(image_path)
    img_tensor = preprocess(img).unsqueeze(0)  # Добавляем batch размерности

    # Прогон через модель
    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = outputs.max(1)
        confidence = torch.nn.functional.softmax(outputs[0], dim=0)[predicted].item()

    # Возвращаем название класса и уверенность
    return labels[predicted], confidence
