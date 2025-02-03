from django.urls import path
from . import views
from homepage.views import homepage


urlpatterns = [
    path('', homepage, name="homepage"),
    path('customer/', views.customer_list, name="customer"),
    path('customer/<uuid:id>/edit/', views.customer_list, name="edit_customer_detail"),
    path('customer/save/', views.save_customer, name="save_customer"),
    path('customer/<uuid:id>/delete/', views.delete_customer, name="delete_customer"),
]


# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('customer/',views.customer,name="customer"),
#     path('customer/<uuid:id>',views.customer,name="customer"),
# ]