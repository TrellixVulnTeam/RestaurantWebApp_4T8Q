from django.urls import path, include 
from django.contrib.auth import views as auth_views

from . import views

#namespace
app_name = 'BasicBusinessManager'
urlpatterns = [
    path('en/', views.MainView.as_view(), name='main'),
    path('en/login/', views.login_view, name='login'),
    path('en/logout/', views.logout_view, name='logout'),
    path('en/contact/', views.ContactView.as_view(), name='contact'),
    #path('en/', auth_views.LoginView.as_view(template_name='BasicBusinessManager/WebHtmls/EN/Main.html')),
     # ex: /polls/5/
    #path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # ex: /polls/5/results/
    #path('product/<int:product_id>/reviews/', views.reviews, name='reviews'),
    # ex: /polls/5/add_review/
    #path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    # ex: /polls/5/
    #path('product/<int:product_id>/review/', views.review, name='review'),
]