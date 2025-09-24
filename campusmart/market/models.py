from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('books', 'Books'),
    ('electronics', 'Electronics'),
    ('furniture', 'Furniture'),
    ('others', 'Others'),
]

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='others')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images/')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

