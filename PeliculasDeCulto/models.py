from django.db import models
from django.utils.text import slugify
# Create your models here.

class PeliculasDeCulto(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="",null = False, primary_key=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

