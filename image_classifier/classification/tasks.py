import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "image_classifier.settings")

import django
django.setup()


import dramatiq
from classification.models import UploadedImage
from classification.some_ml_library import classify  # Подключите библиотеку для классификации изображений
from classification.google_drive_utils import upload_to_drive
import logging

logger = logging.getLogger(__name__)

@dramatiq.actor
def classify_image(image_id):
    image_instance = UploadedImage.objects.get(id=image_id)
    result, confidence = classify(image_instance.image.path)
    image_instance.classification = result
    image_instance.confidence = confidence
    image_instance.save()
    logger.info(f"Классификация завершена для изображения {image_instance.id}")

    # Загрузка в Google Drive
    upload_to_drive(image_instance.image.path, image_instance.image.name)