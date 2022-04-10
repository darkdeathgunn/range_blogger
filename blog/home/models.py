from operator import imod
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .utils import *

class Blogmodel(models.Model):
    title=models.CharField(max_length=1000)
    content=FroalaField()
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='blogimg')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blogmodel, self).save(*args, **kwargs)