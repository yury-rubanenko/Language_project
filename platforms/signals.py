from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import Tag, Word


# перевірка на тег присвоєння дефолтого тегу
@receiver(post_save, sender=Word)
def assign_default_tag(sender, instance, created, **kwargs):
    if created and not instance.tags.exists():
        default_tag, created = Tag.objects.get_or_create(name="tag_not_set")
        instance.tags.add(default_tag)


@receiver(m2m_changed, sender=Word.tags.through)
def update_word_tags(sender, instance, action, **kwargs):
    if action == "post_remove":
        if not instance.tags.exists():
            default_tag, created = Tag.objects.get_or_create(name="tag_not_set")
            instance.tags.add(default_tag)

    if action == "post_add":
        if not instance.tags.exists():
            default_tag, created = Tag.objects.get_or_create(name="tag_not_set")
            instance.tags.add(default_tag)
