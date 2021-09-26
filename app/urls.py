from django.urls import path
from . import views
urlpatterns = [
    path('',views.ReportView.as_view(),name='report_list_view'),
    
    path('product',views.ProductView.as_view(),name='product_list_view'),
    path('product-edit/<str:pk>',views.ProductUpdateView.as_view(),name='product_update_view'),
    path('product-create/',views.ProductCreateView.as_view(),name='product_create_view'),

    path('location',views.LocationView.as_view(),name='location_list_view'),
    path('location-edit/<str:pk>',views.LocationUpdateView.as_view(),name='location_update_view'),
    path('location-create/',views.LocationCreateView.as_view(),name='location_create_view'),

    path('movement',views.MovementView.as_view(),name='movement_list_view'),
    path('movement-edit/<str:pk>',views.MovementUpdateView.as_view(),name='movement_update_view'),
    path('movement-create/',views.MovementCreateView.as_view(),name='movement_create_view'),
    path('move-to/<str:pk>',views.MovementToView.as_view(),name='movement_to_view'),
    path('move-out/<str:pk>',views.MovementOutView.as_view(),name='movement_out_view'),


]