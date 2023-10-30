from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Subject(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Subject, on_delete=models.PROTECT, related_name='subject')
    content = models.CharField(max_length=50000, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    tags = ArrayField(models.CharField(max_length=20, blank=True))

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='lesson')
    comment = models.CharField(max_length=2000, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id
