from django.db import models


class Voter(models.Model):
    identity = models.IntegerField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    location = models.CharField(max_length=20)

    objects: models.Manager()


class Choice(models.Model):
    cidentity = models.IntegerField()
    choice = models.CharField(max_length=5)


class Vote(models.Model):
    identity = models.IntegerField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    location = models.CharField(max_length=20)
    dob = models.CharField(max_length=10)

    objects: models.Manager()


class Option(models.Model):
    cidentity = models.IntegerField()
    choice = models.CharField(max_length=5)

    objects: models.Manager()
