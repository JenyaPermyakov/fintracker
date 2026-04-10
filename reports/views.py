from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from transactions.models import Transaction
from django.db.models.functions import TruncDate


class CategoryReportView(APIView):
    def get(self, request):
        data = Transaction.objects.filter(
            user=request.user,
            type='expense'
        ).values('category__name').annotate(
            total=Sum('amount')
        ).order_by('-total')

        return Response(data)


class TimeSeriesReportView(APIView):
    def get(self, request):
        data = Transaction.objects.filter(
            user=request.user,
            type='expense'
        ).annotate(
            day=TruncDate('created_at')
        ).values('day').annotate(
            total=Sum('amount')
        ).order_by('day')

        return Response(data)