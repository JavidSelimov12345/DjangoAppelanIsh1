from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categories(models.Model):
    Categori_name=models.CharField(max_length=50,verbose_name='Kateqoriya',)

    def __str__(self):
        return self.Categori_name


class Elan(models.Model):
    title=models.CharField(max_length=100,verbose_name='Basliq')
    company_name=models.CharField(max_length=100,verbose_name='Müəsisə adı')
    company_email=models.CharField(max_length=50,verbose_name='email')
    job_type=models.CharField(max_length=50,verbose_name='işin tipi',blank=True)
    salary = models.CharField(max_length=50,verbose_name='maaş',blank=True)
    job_category= models.ForeignKey(
        'elan.Categories',on_delete=models.CASCADE,null=True
    )
    experience=models.CharField(max_length=50,verbose_name='Iş təcrübəsi')
    start_date=models.DateTimeField(auto_now=True,null=True)
    end_date=models.DateField(null=True)
    job_description=RichTextField(null=True)
    job_requirements=RichTextField(null=True)
    image_field=models.ImageField(upload_to='images/',null=True)

    class Meta:
        ordering=('-start_date',)
   

    def __str__(self):
        return self.title



