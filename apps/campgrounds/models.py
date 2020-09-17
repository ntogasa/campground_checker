from django.db import models


# Create your models here.
class Campground(models.Model):
    camp_id = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


class Log(models.Model):
    date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(null=True)
    start_id = models.IntegerField(default=None)
    end_id = models.IntegerField(default=None)

    class Meta:
        ordering = ['date']