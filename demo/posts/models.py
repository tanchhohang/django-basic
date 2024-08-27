from django.db import models

# Create your models here.
# for databases

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.jpg', blank=True)

    def __str__(self) -> str:
        return self.title

