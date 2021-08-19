from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token), ##sending a username/pw to this url will return a JWT if the user is valid
    path('register/', views.RegisterViewSet.as_view())
]