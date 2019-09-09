from django.db import models

# Create your models here.
class Omikuji(models.Model):
    name = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Omikuji_items(models.Model):
    omikuji_id = models.ForeignKey(Omikuji, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
