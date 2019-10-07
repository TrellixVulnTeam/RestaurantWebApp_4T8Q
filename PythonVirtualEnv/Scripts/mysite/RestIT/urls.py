from django.urls import path

from . import views

urlpatterns = [
    path('product/all/', views.index, name='index'),
     # ex: /polls/5/
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # ex: /polls/5/results/
    path('product/<int:review_id>/review/', views.reviews, name='reviews'),
    # ex: /polls/5/add_review/
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
]