from django.urls import path

from apis.products.views import ListCategoryAPIView, list_category, home, create_products, create_category, create_sub_category, detail_product, update_product


urlpatterns = [
    path('', ListCategoryAPIView.as_view()),
    path('list/', list_category),
    path('home/', home, name='home'),
    path('detail_product/<int:id>/<str:slug>/', detail_product, name='detail_product'),
    path('detail_product/<int:id>/<str:slug>/update/', update_product, name='update_product'),
    path('create_products/', create_products, name='create_products'),
    path('create_category/', create_category, name='create_category'),
    path('create_sub_category/', create_sub_category, name='create_sub_category'),
]
