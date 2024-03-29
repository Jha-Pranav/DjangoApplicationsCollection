from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=350)
    pub_date = models.DateField('Date Published')

    def was_published_recently(self):
        now = timezone.now()
        diff = now - datetime.timedelta(days=1)
        return  diff.date() <= self.pub_date <= now.date()
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
