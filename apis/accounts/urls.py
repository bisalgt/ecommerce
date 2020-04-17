from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from apis.accounts.views import SignUpView, user_detail, user_update

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    # path("<int:id>/<str:slug>/update/", UserUpdateView.as_view(), name="update_user"),
    path("<int:id>/<str:slug>/update/", user_update, name="update_user"),
    path("<int:id>/<str:slug>/", user_detail, name="user_detail"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
]
