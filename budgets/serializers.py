from rest_framework import serializers
from .models import Budget
from django.db.models import Sum
from transactions.models import Transaction

class BudgetSerializer(serializers.ModelSerializer):
    spent = serializers.SerializerMethodField()
    remaining = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = '__all__'

    def get_spent(self, obj):
        total = Transaction.objects.filter(
            user=obj.user,
            category=obj.category,
            type='expense',
            created_at__year=obj.month.year,
            created_at__month=obj.month.month
        ).aggregate(total=Sum('amount'))['total']

        return total or 0

    def get_remaining(self, obj):
        spent = self.get_spent(obj)
        return obj.limit - spent