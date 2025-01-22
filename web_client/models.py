from django.db import models
from ckeditor.fields import RichTextField

class TextEntry(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    content = models.TextField(default="Write text here...")
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
