from django.urls import path
import public.views as views

urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
    path('about', views.AboutView.as_view(), name='About'),
    path('tours', views.ToursView.as_view(), name='Tours'),
]
