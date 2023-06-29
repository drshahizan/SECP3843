from django.contrib import admin
from django.urls import path, include
from q3_app.views import user_registration, login_view, customer_dashboard_view, technical_worker_dashboard_view, management_dashboard_view,customer_dashboard,inspections_by_sector,inspections_by_month

urlpatterns = [
    path('customer_dashboard/', customer_dashboard_view, name='customer_dashboard'),
    path('customer_predict/', customer_dashboard, name='customer_predict'),
    path('technical_worker_dashboard/', technical_worker_dashboard_view, name='technical_worker_dashboard'),
    path('inspections_by_sector/', inspections_by_sector, name='inspections_by_sector'),
    path('inspections_by_month/', inspections_by_month, name='inspections_by_month'),
    path('management_dashboard/', management_dashboard_view, name='management_dashboard'),
    path('', login_view, name='home'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('register/', user_registration, name='user_registration'),
]
