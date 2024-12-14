from django.urls import path
from . import views  # Fixed import statement

urlpatterns = [
    path('login/', views.route_manager_login, name='route_manager_login'),
    path('manager', views.route_manager_home, name='route_manager_home'),
    path('api/create_route/', views.create_route, name='create_route'),
    path('api/get_route/<int:route_id>/', views.get_route, name='get_route'),
    path('assign_route/<int:bus_id>/', views.assign_route_to_driver, name='assign_route_to_driver'),
    path('routes/', views.route_list, name='route_list'),  # Added route list
  
    path('save-route/', views.save_route, name='save_route'),
 

    
    path('empty-page/', views.empty_page, name='empty_page'),


]
