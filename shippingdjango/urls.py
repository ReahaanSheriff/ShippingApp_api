from django.urls import path
from . import views
from knox.views import LogoutView
from knox import views as knox_views

urlpatterns = [
    path('',views.createShipment),
    path('getshipment/<str:pk>',views.getShipment),
    path('trackAllShipment/',views.trackAllShipment),
    path('trackOneShipment/<str:fk>',views.trackOneShipment),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
    path('currentuser/',views.current_user),
    path('deletetokens/',views.deletetokens),
    path('userShipment/',views.userShipment)
]
