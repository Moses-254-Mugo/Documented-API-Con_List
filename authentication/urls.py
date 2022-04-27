from django.urls import path
from .views import ReigsterView

urlpatterns =[
    path('register', ReigsterView.as_view())
]
