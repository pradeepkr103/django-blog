# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import blog,Comment_block

# Register your models here.
admin.site.register(blog)
# admin.site.register(Like_button)
admin.site.register(Comment_block)
