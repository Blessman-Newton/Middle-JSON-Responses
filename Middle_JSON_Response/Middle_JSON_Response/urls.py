from django.contrib import admin
from django.urls import path
from day_two import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/', views.json_view, name='json_view'),
]
