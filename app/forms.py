# SPDX-FileCopyrightText: 2025 Imran Mustafa <imran@imranmustafa.net>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django.forms import ModelForm
from app.models import Paste

class PasteForm(ModelForm):
    class Meta:
         model = Paste
         fields = ["content"]
