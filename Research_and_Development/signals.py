from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ResearchAndDevelopment
import os

@receiver(pre_delete, sender=ResearchAndDevelopment)

def delete_image_files(sender, instance, **kwargs):
    # Delete the image file from the file system
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
