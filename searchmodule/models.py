from django.contrib import admin
from django.db import models

# Create your models here.

class Category(models.Model):
    Type = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.Type
    
    
class Publicdb(models.Model):
    Id   = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Desc = models.TextField()
    Mrp  = models.CharField(max_length=255)
    Crp  = models.CharField(max_length=255)
    Qty  = models.CharField(max_length=255)
    Url  = models.CharField(max_length=255)
    Category  = models.ForeignKey(Category)
    
    def __unicode__(self):
        return unicode(self.Id)
    
    
class RawPublicdb(models.Model):
    Id   = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Desc = models.CharField(max_length=255)
    Mrp  = models.CharField(max_length=255)
    Qty  = models.CharField(max_length=255)
    Variety = models.CharField(max_length=255)
    Crp  = models.CharField(max_length=255)
    RemoteUrl = models.CharField(max_length=255)
    Url  = models.CharField(max_length=255)
    Category  = models.CharField(max_length=255)
    Hsh  = models.CharField(max_length=255)
    
    def __unicode__(self):
        return unicode(self.Id)
    
admin.site.register(Category)    
admin.site.register(Publicdb)
admin.site.register(RawPublicdb)
