from django.db import models

class details(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    city=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
