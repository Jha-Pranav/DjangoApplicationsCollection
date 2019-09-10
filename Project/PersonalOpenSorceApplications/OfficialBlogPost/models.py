from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    creation_time = models.DateField(default=timezone.now)
    pub_date = models.DateField(blank=True,null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self):
        return reverse('post_detail')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('OfficialBlogPost.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    creation_time = models.DateField(default=timezone.now)
    approve_date = models.BooleanField(default=False)

    def approve(self):
        self.approve_date = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text