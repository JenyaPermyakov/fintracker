from django_filters import rest_framework as filters
from .models import Transaction


class TransactionFilter(filters.FilterSet):
    from_date = filters.DateFilter(
        field_name="created_at",
        lookup_expr='gte'
    )

    to_date = filters.DateFilter(
        field_name="created_at",
        lookup_expr='lte'
    )

    class Meta:
        model = Transaction
        fields = ['category', 'type']