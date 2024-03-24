from django.urls import path

from travel.views import TravelWriteView, TravelDetailView

app_name = 'travel'

urlpatterns = [
    path('write/', TravelWriteView.as_view(), name='write'),
    path('detail/', TravelDetailView.as_view(), name='detail')
]