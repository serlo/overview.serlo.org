from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=200)
    sherpa = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name='sherpee')

    def __str__(self):
        return self.name


class Email(models.Model):
    address = models.EmailField(max_length=254, blank=True)
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='work_emails')


class Phone(models.Model):
    number = PhoneNumberField(blank=True)
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='work_phone_numbers')


class TimeStamp(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=200)
    lama = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='project_lama')
    members = models.ManyToManyField(Member, related_name='project_members')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=200)
    lama = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='unit_lama')
    members = models.ManyToManyField(Member, related_name='unit_members')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
