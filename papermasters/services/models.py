from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from tinymce.models import HTMLField



STATUS_CHOICES = (
    ('ur', 'Urgent'),
    ('ac', 'Acceptable'),
    ('op', 'Optimized'),
)
class Service(models.Model):
    status = models.CharField(max_length=200, blank=True, null=True, choices=STATUS_CHOICES)
    title = models.CharField(max_length=200, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=200, null = True, unique = True, blank = True)
    meta_title = models.CharField(max_length=200, blank=True) 
    meta_description = models.CharField(max_length=400)
    content = HTMLField(blank=True, null=True)
    notes = models.TextField(null = True, blank=True)
    img_src = models.CharField(max_length=255, blank=True, null=True)
    img_alt = models.CharField(max_length=255, blank=True,null=True)
    img_name = models.CharField(max_length=255, blank=True,null=True) 


    class Meta:
            verbose_name = 'Service'
            verbose_name_plural = 'Services'
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('services:services', args=[str(self.slug)])