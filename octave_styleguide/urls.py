from django.urls import path
from django.conf import settings

from lib.octave_styleguide.octave_styleguide import views

urlpatterns = []

app_name = 'styleguide'

if settings.DEBUG:
    urlpatterns += [
        path('styleguide/', views.StyleguideView.as_view(), name='index'),
        path('styleguide/<slug:template_name>/', views.StyleguideView.as_view(), name='detail'),
    ]
