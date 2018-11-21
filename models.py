# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='pic/', blank=True, null=True)
    short_desc = models.CharField(max_length=150, blank=True, null=True)
    content = RichTextUploadingField()
    create_date = models.DateTimeField(auto_now_add=True)
    comment = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment_block(models.Model):
		info = models.ForeignKey(blog)
		name = models.CharField(max_length=20, null=True, blank=True)
		comment = models.CharField(max_length=500)
		user = models.CharField(max_length=20, null=True, blank=True)
