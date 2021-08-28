from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.LabListAPIView.as_view(), name="all-labs"),
     path('<str:id>', views.LabRetrieveAPIView.as_view(), name="single-lab"),
     path('create/',views.LabCreateAPIView.as_view(),name="lab-create"),
     path('update/<str:id>',views.LabUpdateAPIView.as_view(),name="lab-update")
]