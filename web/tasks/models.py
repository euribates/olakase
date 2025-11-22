from django.db import models

from utils.texts import slugify


class Task(models.Model):

    class Meta:
        ordering = ['-urgent']

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    urgent = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def load_task(cls, id_task: int):
        try:
            return cls.objects.get(pk=id_task)
        except cls.DoesNotExist:
            return None


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
