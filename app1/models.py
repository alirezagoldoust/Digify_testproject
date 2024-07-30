from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name="orders")
    cost = models.PositiveIntegerField()
    primary_cost = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=32, 
        choices=[
            ("initial","initial"),
            ("paid", "paid"),
            ("sent", "sent"),
        ]
    )
    
    def __str__(self) -> str:
        return str(self.id) + "-" + self.store.name