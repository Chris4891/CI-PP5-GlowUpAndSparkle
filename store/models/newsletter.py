from django.db import models
from ckeditor.fields import RichTextField

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    

