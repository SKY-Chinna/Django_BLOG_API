from django.db import models

# Create your models here.




class Product(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100, blank=True, default='')
    Author = models.CharField(max_length=100, blank=True, default='')
    Description = models.TextField()
    size = models.IntegerField(default=False)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    Quality = models.CharField(max_length=1, choices=SHIRT_SIZES, default=True)
    



    def __str__(self):
        return self.title
