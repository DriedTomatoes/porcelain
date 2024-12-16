from django.urls import include, path

from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path("register", RegisterAPIView.as_view()),
    path("login", LoginAPIView.as_view()),

]