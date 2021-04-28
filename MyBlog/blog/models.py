from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name = 'comments', on_delete=models.DO_NOTHING)
    author = models.CharField(max_length = 200)    
    text = models.TextField()
    creation_date = models.DateTimeField(default = timezone.now())
    approved_comments = models.BooleanField(default = False)


    def approve(self):
        self.approved_comments = True
        self.save()


    
    
    def __str__(self):
        return self.text

    






