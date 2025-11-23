from django.db import models

from utils.texts import slugify


class Priority(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    representation = models.CharField(max_length=18)
    level = models.IntegerField()

    def __str__(self):
        return self.representation

    @classmethod
    def load_priority(cls, id_priority: int):
        try:
            return cls.objects.get(pk=id_priority)
        except cls.DoesNotExist:
            return None




class Task(models.Model):

    class Meta:
        ordering = ['-priority__level']

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    priority = models.ForeignKey(Priority,
        default='NOR',
        related_name='tasks',
        on_delete=models.PROTECT,
        )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def load_task(cls, id_task: int):
        try:
            return cls.objects.get(pk=id_task)
        except cls.DoesNotExist:
            return None

    @property
    def urgent(self) -> bool:
        return self.priority_id in {'URG', 'CRI'}

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
