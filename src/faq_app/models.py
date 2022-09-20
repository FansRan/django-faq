"""
Django model definition
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    """Model definition for Question."""

    question = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'question'
        ordering = ['updated_at']

    def __str__(self):
        """Unicode representation of Question."""
        return str(self.question)



class Answer(models.Model):
    """Model definition for Answer."""
       
    answer = models.TextField()
    question = models.ForeignKey(Question,  related_name='answers', on_delete=models.CASCADE)
    client = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Answer."""

        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answer'
        ordering = ['updated_at']

    def __str__(self):
        """Unicode representation of Answer."""
        return str(self.answer)
