from django.urls import path
from identify.views import IdentifyView

urlpatterns = [
    path('identify/', IdentifyView.as_view(), name='identify'),
]
