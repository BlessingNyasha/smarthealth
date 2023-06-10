from django.urls import path
from smarthealth import views

urlpatterns = [
    
    path ("index",views.login, name="index"),
    path ("register/",views.register, name="register"),
    path ("home", views.home, name="home" ),
    path ("ecg", views.ecg, name="ecg" ),
    path ("lung/", views.lung, name="lung" ),
    path ("faq", views.faq, name="faq" ),
    path("results", views.results, name="results"),
    path("resultspi", views.resultspi, name="resultspi"),
    path("read", views.read, name="read"),
    path("spirometry", views.spirometry, name="spirometry"),
   path("contact", views.contact, name="contact"),
   path("doctors", views.doctors, name="doctors"),
   path('doctors/<int:doctor_id>/contact/', views.doctors, name='doctor_contact'),
   path('chart_image/<int:record_id>/', views.chart_image, name='chart_image'),
    
]
