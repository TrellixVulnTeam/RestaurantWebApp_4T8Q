from django.urls import path

from . import views

#namespace
app_name = 'RestIT'
urlpatterns = [
    path('product/all/', views.index, name='index'),
     # ex: /polls/5/
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # ex: /polls/5/results/
    path('product/<int:product_id>/reviews/', views.reviews, name='reviews'),
    # ex: /polls/5/add_review/
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    # ex: /polls/5/
    path('product/<int:product_id>/review/', views.review, name='review'),
]