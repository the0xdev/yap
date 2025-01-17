# SPDX-FileCopyrightText: 2025 Imran Mustafa <imran@imranmustafa.net>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

class Paste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
