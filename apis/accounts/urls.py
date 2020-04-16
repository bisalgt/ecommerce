from django.urls import path

from apis.accounts.views import create_user

urlpatterns = [
    path('', create_user),
]
