from django.urls import path
from .views import CategoryReportView, TimeSeriesReportView

urlpatterns = [
    path('reports/categories/', CategoryReportView.as_view()),
    path('reports/timeseries/', TimeSeriesReportView.as_view()),
]