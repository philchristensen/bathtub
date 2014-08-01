from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __unicode__(self):
        return self.title
