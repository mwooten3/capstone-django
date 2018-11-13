# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import MaxExtent, MaxExtentPlot # from waterExplorer.models, import MaxExtent model

# Register your models here.
admin.site.register(MaxExtent)
admin.site.register(MaxExtentPlot)
