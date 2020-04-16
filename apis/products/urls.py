from django.urls import path

from apis.products.views import ListCategoryAPIView, list_category, list_ct



urlpatterns = [
    path('', ListCategoryAPIView.as_view()),
    path('list/', list_category),
    path('lict/', list_ct),
]
