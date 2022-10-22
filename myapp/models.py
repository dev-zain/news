from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class Category(models.Model):
    # photo = models.ImageField(upload_to='images',null=True,blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class News(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    body = RichTextField()
    slug = models.SlugField(max_length=200)
    category=models.ForeignKey('Category',related_name='posts', on_delete=models.SET_NULL,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.title