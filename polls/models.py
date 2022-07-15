from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=500)

    def __str__(self):
        return self.question

class Choise(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choises')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option
        