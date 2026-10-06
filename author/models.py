from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100,null=False,blank=False)
    last_name = models.CharField(max_length=100,null=False,blank=False)
    dob = models.DateField(null=True,blank=True)
    year_of_death = models.DateField(null=True,blank=True)

    # @property
    # def age(self):
    #     self.age=self.year_of_death - self.dob

    def __str__(self):
        return f"{self.first_name} {self.last_name}"