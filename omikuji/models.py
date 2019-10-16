from django.db import models

# Create your models here.
class Omikuji(models.Model):
    name = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Omikuji_items(models.Model):
    # omikuji_id = models.ForeignKey(Omikuji, on_delete=models.CASCADE)
    omikuji = models.ForeignKey(
        Omikuji,
        on_delete=models.PROTECT,
        null=True
    )
    item_name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
