from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)

    limit = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

    class Meta:
        unique_together = ('user', 'category', 'month')

    def __str__(self):
        return f"{self.category} - {self.amount}"