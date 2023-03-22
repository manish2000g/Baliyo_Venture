from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import HeroSections, ServiceLists, PortfolioLists
import os

@receiver(pre_delete, sender=HeroSections)
@receiver(pre_delete, sender=ServiceLists)
@receiver(pre_delete, sender=PortfolioLists)
def delete_image_files(sender, instance, **kwargs):
    # Delete the image file from the file system
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
