from django.db import models
from datetime import datetime

class DeicideList(models.Model):
    Gods_Name = models.CharField(max_length=20)
    Accusation = models.CharField(max_length=65)
    created_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % (self.Gods_Name, self.Accusation)

class DeicideListArchive(models.Model):
    Gods_Name = models.CharField(max_length=20)
    Accusation = models.CharField(max_length=65)
    created_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s - %s - %s' % (self.Gods_Name, self.Accusation, self.created_date)

