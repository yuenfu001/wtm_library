from django.db import models
# from author.models import Author
# Create your models here.

class Genre(models.Model):
    CHOICES = (
        ("Fiction","Fiction"),
        ("Non-Fiction","Non-Fiction"),
        ("Science Fiction","Science Fiction"),
        ("Fantasy","Fantasy"),
        ("Mystery","Mystery"),
        ("Romance","Romance"),
        ("Horror","Horror"),
        ("Thriller","Thriller"),
        ("Biography","Biography"),
        ("History","History"),
        ("Self-Help","Self-Help"),
        ("Academic","Academic/Special"),
    )
    title = models.CharField(max_length=200,blank=False,null=False)
    category = models.CharField(max_length=200,choices=CHOICES,blank=False,null=False)

    def __str__(self):
        return f"{self.title}"