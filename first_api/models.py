from django.db import models

class Skill(models.Model):
  name = models.CharField(max_length=100)
  level = models.IntegerField()

  def __str__(self):
    return self.name

class App(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()

  def __str__(self):
    return self.name

class Album(models.Model):
  name = models.CharField(max_length=100)
  url = models.CharField(max_length=100)
  year = models.IntegerField(null=True)

  def __str__(self):
    return self.name