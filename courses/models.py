from django.db import models

# Create your models here.

class Axis(models.Model):
    description = models.CharField(max_length=200)


class Goal(models.Model):
    axis = models.ForeignKey(Axis)
    description = models.CharField(max_length=200)

    
class Course(models.Model):
    content = models.TextField
    goal = models.ForeignKey(Goal)


class Poll(models.Model):
    questions = models.ManyToManyField(Question)
    goal = models.ForeignKey(Goal)


class Question(models.Model):
    text = models.CharField(max_length=200)
