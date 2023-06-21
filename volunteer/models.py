from django.db import models
from django.urls import reverse

from config import settings

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True)

    class Meta:
        ordering =['name']
        verbose_name = 'region'
        verbose_name_plural = 'regions'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('volunteer:place_in_region', args=[self.slug])

class Place(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='places')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='places/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-region']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('volunteer:place_detail', args=[self.id, self.slug])
