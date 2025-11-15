## Modelos

Dado que el proyecto es un gestor de tareas vamos a trabajar sobre todo
con el modelo `tasks.Task`, que se describe inicialmente así:


```python
class Task(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

