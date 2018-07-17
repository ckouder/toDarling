from django.db import models

# Create your models here.
class IwantToSay(models.Model):
    def __str__ (self):
        return self.title

    title = models.CharField(max_length=1000)
    words = models.TextField(max_length=1000)
    animate = models.CharField(choices = (
        ('fadeIn', 'fade in'),
        ('bounceIn', 'bounce in'),
        ('fadeInDown', 'fade in down'),
        ('fadeInUp', 'fade in up'),
        ('fadeInLeft', 'fade in left'),
        ('fadeInRight', 'fade in right'),
        ('rollIn', 'roll in'),
    ), max_length=20)
