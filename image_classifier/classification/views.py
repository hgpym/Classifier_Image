from django.shortcuts import render, redirect
from classification.forms import UploadImageForm
from classification.models import UploadedImage
from classification.tasks import classify_image

def upload_image(request):
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            classify_image.send(image_instance.id)  # Отправляем задачу в очередь
            return redirect('result', pk=image_instance.id)
    else:
        form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})

def result(request, pk):
    image = UploadedImage.objects.get(pk=pk)
    image.refresh_from_db()
    return render(request, 'result.html', {'image': image})
