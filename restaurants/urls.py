from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('food/edit/<int:pk>/', views.edit_food_item, name='edit_food_item'),
    path('food/delete/<int:pk>/', views.delete_food_item, name='delete_food_item'),
    path('add-food/', views.add_food_item, name='add_food_item'),

]
