from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from exhibition import views
from exhibition.views import ExhibitionWriteView, ExhibitionDetailView, ExhibitionFileDownloadView, ExhibitionListView, \
    ExhibitionUpdateView

app_name = 'exhibition'

urlpatterns = [
    path('write/', ExhibitionWriteView.as_view(), name='write'),
    path('detail/', ExhibitionDetailView.as_view(), name='detail'),
    path('list/', ExhibitionListView.as_view(), name='list'),
    path('update/<int:id>/', ExhibitionUpdateView.as_view(), name='update')

]
