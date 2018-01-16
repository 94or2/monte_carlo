import datetime
from django.db import models
from django.utils import timezone


class Member(models.Model):
    member_name = models.CharField(max_length=80)
    alias_name = models.CharField(max_length=200)

    def __str__(self):
        return self.member_name


class Group(models.Model):
    group_name = models.CharField(max_length=80)
    alias_name = models.CharField(max_length=200)

    def __str__(self):
        return self.group_name


class GroupMemberMap(models.Model):
    group = models.ManyToManyField(Group)
    member = models.ManyToManyField(Member)

