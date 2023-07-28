from django.urls import path
from remove import views
app_name='remove'
urlpatterns=[
    path('', views.remove_pages, name='remove_pages'),
]
