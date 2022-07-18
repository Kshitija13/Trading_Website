from django.urls import path
from home import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/', views.main, name='index'),
    path('charts/', views.charts, name='charts'),
    path(r'investing_chart/', views.indian, name='in'),
    path('tables/', views.tables, name='tables'),
    path(r'login/', views.login1, name='login1'),
    path(r'grid/', views.crypto, name='crypto'),
    # path(r'index/', views.back, name='back'),
]