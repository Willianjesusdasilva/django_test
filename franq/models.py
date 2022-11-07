from django.db import models

# Create your models here.

class client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cellphone = models.PositiveBigIntegerField()
    marketin_validation = models.BooleanField(default=False)
    adress = models.CharField(max_length=255,null=True)
    profession = models.CharField(max_length=255,null=True)
    document = models.PositiveBigIntegerField(null=True)

    def __str__(self) -> str:
        return self.name