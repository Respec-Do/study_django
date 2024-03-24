"""
URL configuration for view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from exhibition.views import ExhibitionFileDownloadView
from main.views import MainView
from view.views import StudentRegisterView, StudentResultView, StudentRegisterFormView, MemberRegisterFormView, \
    MemberRegisterView, MemberResultView, StudentRegister2FormView, StudentRegister2View, StudentResult2View, \
    ProductDetailAPI, ProductDetailView


class TravelResultView:
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('post/', include('post.urls')),
    path('student/register/form/', StudentRegisterFormView.as_view(), name='student-register-form'),
    path('student/register/', StudentRegisterView.as_view(), name='student-register'),
    path('student/result/', StudentResultView.as_view(), name='student-result'),
    path('member/register/form/', MemberRegisterFormView.as_view(), name='member-register-form'),
    path('member/register/', MemberRegisterView.as_view(), name='member-register'),
    path('member/result', MemberResultView.as_view(), name='member-result'),
    path('student/register2/form/', StudentRegister2FormView.as_view(), name='student-register2-form'),
    path('student/register2/', StudentRegister2View.as_view(), name='student-register2'),
    path('student/result2/', StudentResult2View.as_view(), name='student-result2'),
    # path('travel/', include('travel.urls')),
    path('product/detail/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:product_id>/', ProductDetailAPI.as_view(),name='product-detail'),
    path('exhibition/', include('exhibition.urls')),
    path('notification/', include('notification.urls')),
    path('upload/<path:file_path>/', ExhibitionFileDownloadView.as_view(), name='download'),
    path('', MainView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











