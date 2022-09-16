from datetime import datetime
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from Blog.models import *
from slugify import slugify

@receiver(post_save, sender=Blog)
def slug_generator_recipe_model(sender, instance, created, **kwargs):
        replacements = [['Ə', 'e']]
        slug = slugify(instance.title, replacements=replacements) + '-' + str(instance.id)
        if not slug == instance.slug:
            instance.slug = slug
            instance.save()