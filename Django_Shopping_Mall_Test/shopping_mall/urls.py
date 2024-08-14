from django.urls import path

from . import views

app_name = "shopping_mall"

urlpatterns = [
    path("main_page/",views.main_page, name = "main_page"),
    path("product_addition/",views.product_addition , name = "product_addition"),
    path("category/<str:category>/", views.category_page, name = "category_page"),
    path("product_details/<int:product_id>/", views.product_details, name = "product_details"),
    path("cart/",views.cart, name = "cart"),
    path("handle_action/<int:product_id>/", views.handle_action, name = "handle_action"),
    path("bying_product/<int:product_id>/",views.bying_product, name = "bying_product"),
    path("cart_product_delete/<int:product_id>/", views.cart_product_delete,name="cart_product_delete"),
    path("pay_product/<int:product_id>/", views.pay_product, name = "pay_product"),
    
]

