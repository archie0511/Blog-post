from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    
        #add fields for table
        title=models.CharField(max_length=100)
        content=models.TextField()
        date_posted =models.DateTimeField(default=timezone.now)
        author= models.ForeignKey(User,on_delete=models.CASCADE)#one post can have one author

        def __str__(self):
            return self.title
        # when we click on post then it will redirect to detail page of that blog
        def get_absolute_url(self):
            return reverse('post-detail',kwargs={'pk':self.pk})    