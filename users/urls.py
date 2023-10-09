from django.urls import path
from .views import ListUserView, CreateUserView, RetrieveUserView, CreateTokenView

urlpatterns = [
    path('list/', ListUserView.as_view()),
    path('create/', CreateUserView.as_view()),
    path('user/', RetrieveUserView.as_view()),
    path('token/', CreateTokenView.as_view()),
]