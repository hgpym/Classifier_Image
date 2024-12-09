from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    classification = models.CharField(max_length=100, blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
