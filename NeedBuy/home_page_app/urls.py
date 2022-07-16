from django.urls import path

from home_page_app import views  # ignore this import error, all works correct.

urlpatterns = [
    path('', views.view_index, name='main'),
]
