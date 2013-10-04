from django.db import models

# Create your models here.
class Photo(models.Model):
    title       = models.CharField(max_length = 60)
    created     = models.DateTimeField(auto_now_add = True)
    image       = models.ImageField(upload_to="images/")
    description = models.TextField(blank=True, null=True)
    slug        = models.SlugField(max_length=40)

class Gallery(models.Model):
    title       = models.CharField(max_length=60)
    pix         = models.ManyToManyField("Photo", related_name="galleries", verbose_name="pictureslist")
    slug        = models.SlugField(max_length=40)
    
