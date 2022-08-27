from django.db import models
import random
import short_url


# Create your models here.

class Link(models.Model):
    slug = models.SlugField(max_length=20, db_index=True, unique=True, )
    completelink = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        rand = random.randint(100, 999999999)
        while True:
            if not Link.objects.filter(slug=short_url.encode_url(rand)).exists():
                break
        self.slug = short_url.encode_url(rand)
        super(Link, self).save()

    def __str__(self):
        return self.slug
