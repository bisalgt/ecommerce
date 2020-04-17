from django.urls import path

from apis.accounts.views import create_user, update_user

urlpatterns = [
    path('', create_user),
    path('upd/<int:id>/', update_user),
]
