from django.db import models
from datetime import datetime, date
from django.core.validators import MinValueValidator, MaxValueValidator
from listings.models import Listing



# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    description = models.TextField(blank = True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default = datetime.now,blank = True)
    def __str__(self):
        return self.name

class Rating(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    name = models.CharField(max_length=100)
    message = models.TextField('message')
    # stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], related_query_name = "stars")
    stars = models.IntegerField(choices = RATING_CHOICES, blank=True,null = True, default = 3)
    sellerid = models.ForeignKey(Seller, on_delete = models.CASCADE, related_name= "id+")
    date_comment = models.DateField(default = date.today)

