from django.urls import path
from .views import ReigsterView,LoginView

urlpatterns =[
    path('register', ReigsterView.as_view()),
    path('login', LoginView.as_view())
]
