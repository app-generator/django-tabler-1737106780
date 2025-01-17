# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Incent(models.Model):

    #__Incent_FIELDS__
    active release cycle = models.TextField(max_length=255, null=True, blank=True)
    current release scope = models.IntegerField(null=True, blank=True)
    build version = models.TextField(max_length=255, null=True, blank=True)
    total bugs = models.TextField(max_length=255, null=True, blank=True)

    #__Incent_FIELDS__END

    class Meta:
        verbose_name        = _("Incent")
        verbose_name_plural = _("Incent")


class Asset Performance Management(models.Model):

    #__Asset Performance Management_FIELDS__
    active sprint = models.TextField(max_length=255, null=True, blank=True)
    user stories in scope = models.TextField(max_length=255, null=True, blank=True)
    bugs in scope = models.TextField(max_length=255, null=True, blank=True)
    total story points = models.TextField(max_length=255, null=True, blank=True)

    #__Asset Performance Management_FIELDS__END

    class Meta:
        verbose_name        = _("Asset Performance Management")
        verbose_name_plural = _("Asset Performance Management")



#__MODELS__END
