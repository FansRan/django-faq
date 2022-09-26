"""
Django model definition
"""

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class TimeStampable(models.Model):
    """Model definition for Parent TimeStampable."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for TimeStampable."""

        abstract = True
        ordering = ["-updated_at"]


class Question(TimeStampable):
    """Model definition for Question."""

    author = models.EmailField(max_length=150)
    question = models.CharField(
        max_length=255,
        unique=True,
        validators=[RegexValidator(r"^.*\?$", message="Must end with question mark")],
    )

    class Meta(TimeStampable.Meta):
        """Meta definition for Question."""

        verbose_name = "Question"
        verbose_name_plural = "Questions"
        db_table = "question"

    def __str__(self):
        """Unicode representation of Question."""
        return str(self.question)


class Answer(TimeStampable):
    """Model definition for Answer."""

    answer = models.TextField()
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE
    )
    client = models.ForeignKey(User, related_name="answers", on_delete=models.CASCADE)

    class Meta(TimeStampable.Meta):
        """Meta definition for Answer."""

        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        db_table = "answer"

    def __str__(self):
        """Unicode representation of Answer."""
        return str(self.answer)
