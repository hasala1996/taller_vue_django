from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    fechaNacimiento = models.DateTimeField()
    edad = models.IntegerField()    


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    id_author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True,null=True,verbose_name='id del autor el cual está asociado',db_column='id_name')


