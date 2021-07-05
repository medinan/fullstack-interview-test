from django.db import models
from django.utils.translation import gettext_lazy as _


class PullRequest(models.Model):
    class StatusPullRequest(models.TextChoices):
        OPEN = 'open', _('open')
        CLOSED = 'closed', _('closed')
        MERGED = 'merged', _('merged')

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    branch_base = models.CharField(max_length=100)
    branch_compare = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=StatusPullRequest.choices, default=StatusPullRequest.OPEN)
