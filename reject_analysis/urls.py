from django.urls import path
from . import views

app_name = "reject_analysis"

urlpatterns = [
    path('', views.analysis_view, name='analysis'),
    path('charts/bar_chart/', views.bar_chart_view, name='bar_chart'),
    # path('charts/grouped_bar_chart/', views.grouped_bar_chart_view, name='grouped_bar_chart'),
    path('charts/pie_chart/', views.pie_chart_view, name='pie_chart'),

    path('tables/reject_accept_rate/', views.reject_accept_rate_view, name='reject_accept_rate'),
]
