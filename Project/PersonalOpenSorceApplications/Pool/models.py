from django.db import models

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=350)
    pub_date = models.DateField('Date Published')

    def __str__(self):
        return self.question_text


class Choices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
