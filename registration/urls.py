from django.urls import path
from registration import views

urlpatterns = [
    path('creeaza_cont/', views.user_create, name='creeaza_user'),
    path('termeni-si-conditii/', views.term_cond, name='termenisiconditii'),
    path('gdpr/', views.gdpr, name='gdpr'),

]
