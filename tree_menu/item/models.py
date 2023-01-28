from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.AutoField("item_id", unique=True, primary_key=True)
    name = models.CharField("name", max_length=50)
    parent = models.ForeignKey("self", verbose_name="parent_id", null=True, on_delete=models.CASCADE)
    url = models.CharField("url", unique=True, max_length=50)

    def __str__(self):
        return self.name

    def get_children(self):
        return self.item_set.all()

    
    
    