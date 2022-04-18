from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    title_tag = models.CharField(max_length=300, default="Default title tag")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=300,default='nothing')

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list')