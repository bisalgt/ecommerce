from django.urls import path

from apis.products.views import ListCategoryAPIView, list_category, list_ct, create_user



urlpatterns = [
    path('', ListCategoryAPIView.as_view()),
    path('list/', list_category),
    path('create_user/', create_user),
]
