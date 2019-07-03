from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_date = models.DateTimeField('question date', default=timezone.now)

    def __str__(self):
        return self.question_text

    def publish_date(self):
        return self.publish_date()

    def get_answer(self):
        return Answer.objects.get(pk=self.pk).choice


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.__str__() + '  ' + self.choice.__str__()
