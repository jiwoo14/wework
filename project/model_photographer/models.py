from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.TextField()
    image1 = models.ImageField(upload_to = 'images/')
    image2 = models.ImageField(upload_to = 'images/', default='', null=True, blank=True)
    image3 = models.ImageField(upload_to = 'images/', default='', null=True, blank=True)
    image4 = models.ImageField(upload_to = 'images/', default='', null=True, blank=True)
    image5 = models.ImageField(upload_to = 'images/', default='', null=True, blank=True)
    thumbnail = ImageSpecField(source='image1', processors=[ResizeToFill(120,80)], format='JPEG')

    GENDER_CHOICES = (
        ('여성', '여성'),
        ('남성', '남성'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)

    CATEGORY_CHOICES = (
        ('동양풍', '동양풍'),
        ('서양풍', '서양풍'),
        ('고전', '고전'),
        ('현대', '현대'),
    )

    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, null=True)



    def __str__(self):
        return self.title




class Photo(models.Model):
    title = models.TextField()
    image1 = models.ImageField(upload_to = 'images/')
    image2 = models.ImageField(upload_to = 'images/', default='', null=True, blank=True)
    image3 = models.ImageField(upload_to = 'images/', default='', null=True, blank=True)
    image4 = models.ImageField(upload_to = 'images/', default='', null=True, blank=True)
    image5 = models.ImageField(upload_to = 'images/', default='', null=True, blank=True)
    thumbnail = ImageSpecField(source='image1', processors=[ResizeToFill(120,80)], format='JPEG')

    GENDER_CHOICES = (
        ('여성', '여성'),
        ('남성', '남성'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)

    CATEGORY_CHOICES = (
        ('동양풍', '동양풍'),
        ('서양풍', '서양풍'),
        ('고전', '고전'),
        ('현대', '현대'),
    )

    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, null=True)



    def __str__(self):
        return self.title