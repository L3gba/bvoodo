
import datetime
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import default

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_slug = models.SlugField(max_length=40)
    
    def __unicode__(self):
        return self.category_name
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    sport_name = models.CharField(max_length=255)
    sport_description = models.TextField()
    
    def __unicode__(self):
        return self.sport_name
    

class Site(models.Model):
    LOW = 0
    MED = 1
    HIGH = 2
    TOP = 3
    STATUS_CHOICES = (
                      (LOW, 'low'),
                      (MED, 'medium'),
                      (HIGH, 'high'),
                      (TOP, 'top'),
                      )
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    url = models.URLField()
    promo_image = models.ImageField(upload_to="img/")
    rating = models.IntegerField(choices=STATUS_CHOICES, default=LOW)
    
    def __unicode__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    site = models.ForeignKey(Site)
    sport_name = models.ForeignKey(SubCategory)
    date_published = models.DateTimeField('date published', auto_now_add=True)
    url = models.TextField()
    image = models.ImageField(upload_to="img/")
    
    def __unicode__(self):
        return self.title
