from django.db import models


# Create your models here.

class Link(models.Model):
    slug = models.SlugField(max_length=20, db_index=True, unique=True, )
    completelink = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.slug
