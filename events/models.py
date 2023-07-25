from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

# Create your models here.
class Gallery(models.Model):
    caption=models.CharField(max_length=60,default='Caption')
    thumbnail=models.ImageField(upload_to="gallery")

    def save(self):
        super().save()
        img=Image.open(self.thumbnail.path)
        if img.height>384 and img.width>379:
            output_size=(384,379)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

class Testonomials(models.Model):
    name=models.CharField(max_length=100,default='Person Name')
    rating=models.IntegerField()
    comment=models.TextField()

class Event(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=300)
    thumb=models.ImageField(upload_to="eventthumb")
    #content=RichTextUploadingField(default='')
    author=models.CharField(max_length=30)
    slug=models.SlugField(default='no-slug',unique=True,max_length=200)
    startdate=models.DateTimeField()
    enddate=models.DateTimeField()
    timestamp=models.DateTimeField(auto_now_add=True)
    def save(self):
        self.slug=slugify(self.title)
        super(Event,self).save()
        img=Image.open(self.thumb.path)
        if img.height>1024 and img.width>768:
            output_size=(1024,768)
            img.thumbnail(output_size)
            img.save(self.thumb.path)

    def __str__(self):
        return self.title+ ' | '+self.author
    