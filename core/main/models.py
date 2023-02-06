from django.db import models

# Create your models here.


class HomeSlider(models.Model):

    name1 = models.CharField('Home Slider name1', max_length=30)
    name2 = models.CharField('Home Slider name2', max_length=30)
    img = models.ImageField('Home Slider image', upload_to='media')

    def __str__(self) :
        return self. name1
    
    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'


class HomeProducts(models.Model):
    name = models.CharField('Home product name', max_length=30)
    aabout = models.TextField('Home product about')
    img = models.ImageField('Home product image', upload_to='media')
    price = models.IntegerField('Home product price')

    def __str__(self) :
        return self. name
    
    class Meta:
        verbose_name = 'HomeProduct'
        verbose_name_plural = 'HomeProducts'

class Homeabout(models.Model):

    name = models.CharField('Homeabout name', max_length=100)
    name1 = models.CharField('Homeabout name1', max_length=100)
    name2 = models.CharField('Homeabout name2', max_length=1000)
    name3 = models.CharField('Homeabout name3', max_length=100)
    name4 = models.CharField('Homeabout name4', max_length=100)
    name5 = models.CharField('Homeabout name5', max_length=100)
    name6 = models.CharField('Homeabout name6', max_length=100)
    name7 = models.CharField('Homeabout name7', max_length=100)
    name8 = models.CharField('Homeabout name8', max_length=100)
    img = models.ImageField('Homeabout image', upload_to='media')

    def __str__(self) :
        return self. name
    
class OurProducts(models.Model):
    name = models.CharField('ourproduct name', max_length=30)
    about = models.TextField('ourproduct about')
    img = models.ImageField('ourproduct image', upload_to='media')
    price = models.IntegerField('ourproduct price')

    def __str__(self) :
        return self. name
    
    class Meta:
        verbose_name = 'OurProducts'
        verbose_name_plural = 'OurProducts'


    
class AboutOur(models.Model):
    name = models.CharField('aboutour name', max_length=30)
    name1 = models.CharField('aboutour name1', max_length=30)
    about = models.TextField('aboutour about')
    img = models.ImageField('aboutour image', upload_to='media')
    

    def __str__(self) :
        return self. name
    
    class Meta:
        verbose_name = 'AboutOur'
        verbose_name_plural = 'AboutOur'

class AboutTeam(models.Model):
    name = models.CharField('aboutteam name', max_length=30)
    name1 = models.CharField('abouteam name1', max_length=30)
    about = models.TextField('aboutteam about')
    img = models.ImageField('abouteam image', upload_to='media')
    

    def __str__(self) :
        return self. name

class AboutHappy(models.Model):
    name = models.CharField('abouthappy name', max_length=30)
    about = models.TextField('abouthappy about')
    name1 = models.CharField('abouthappy name1', max_length=30)
    
    def __str__(self) :
        return self. name

class AboutPart(models.Model):
    img = models.ImageField('aboutpart image', upload_to='media')

    

class ContactUs(models.Model):
    name = models.CharField('contactus name', max_length=30)
    
    about = models.TextField('contactus about')
    
    

    def __str__(self) :
        return self. name