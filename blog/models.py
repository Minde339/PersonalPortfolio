from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog/images')
    url = models.URLField(blank=True,max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title
# Create your models here.
