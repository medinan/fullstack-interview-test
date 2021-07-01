from django.db import models


class PullRequest(models.Model):
    title = models.CharField(max_length=150)
