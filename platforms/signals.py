from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import Tag, Word


@receiver(post_save, sender=Word)
def assign_default_tag(sender, instance, created, **kwargs):
    if created and not instance.tags.exists():
        default_tag, created = Tag.objects.get_or_create(name="tag_not_set")
        instance.tags.add(default_tag)


@receiver(m2m_changed, sender=Word.tags.through)
def update_word_tags(sender, instance: Word, action: str, **kwargs):
    if action == "post_remove":
        if not instance.tags.exists():
            default_tag, created = Tag.objects.get_or_create(name="tag_not_set")
            instance.tags.add(default_tag)

    elif action == "post_add":
        instance.tags.through.filter(word_id=instance.id, tag__name="tag_not_set").delete()
        # default_tag, created = Tag.objects.get_or_create(name="tag_not_set")
        # if default_tag in instance.tags.all():
        #     instance.tags.remove(default_tag)
