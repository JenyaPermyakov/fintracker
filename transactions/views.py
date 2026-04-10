from rest_framework.viewsets import ModelViewSet
from .models import Transaction
from .serializers import TransactionSerializer
from .filters import TransactionFilter

class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)