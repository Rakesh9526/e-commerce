from django.urls import path

from e_app import views
app_name="e_app"

urlpatterns=[
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='products_in_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.productdetails,name='products_details'),

]