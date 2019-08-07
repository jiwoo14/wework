from django.contrib import admin
from .models import Post, Photo

# Register your models here.


class PostAdmin(admin.ModelAdmin):
     list_filter = ('gender', 'category')


class PhotoAdmin(admin.ModelAdmin):
     list_filter = ('gender', 'category')

admin.site.register(Post, PostAdmin)
admin.site.register(Photo, PhotoAdmin)