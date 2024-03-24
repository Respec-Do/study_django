from django.contrib import admin
from django.urls import path, include

from member.views import MemberJoinView, MemberLoginView, MemberLogoutView, AdminMemberLoginView, AdminMainView, \
    AdminMainUserView, AdminMainNotificationView, AdminMainInquiryView, AdminMainPaymentView, AdminMainExhibitionView, \
    AdminMainNotificationWriteView, AdminNotificationListAPI, soft_delete, AdminMainUserListAPI, translate, \
    AdminMainExhibitionListAPI, soft_delete_exhibition

app_name = 'member'

urlpatterns = [
    path('join/', MemberJoinView.as_view(), name='join'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('logout/', MemberLogoutView.as_view(), name='logout'),
    path('admin_login/', AdminMemberLoginView.as_view(), name='admin_login'),
    path('admin_main/', AdminMainView.as_view(), name='admin_main'),
    path('admin_main_user/', AdminMainUserView.as_view(), name='admin_main_user'),
    path('admin_main_user/<int:page>/', AdminMainUserListAPI.as_view(), name='admin_main_user_list'),
    path('admin_main_notification/', AdminMainNotificationView.as_view(), name='admin_main_notification'),
    path('admin_main_inquiry/', AdminMainInquiryView.as_view(), name='admin_main_inquiry'),
    path('admin_main_payment/', AdminMainPaymentView.as_view(), name='admin_main_payment'),
    path('admin_main_exhibition/', AdminMainExhibitionView.as_view(), name='admin_main_exhibition'),
    path('admin_main_exhibition/<int:page>/', AdminMainExhibitionListAPI.as_view(), name='admin_main_exhibition_list'),
    path('admin_main_notification_write/', AdminMainNotificationWriteView.as_view(), name='admin_main_notification_write'),
    path('admin_main_notification/<int:page>/', AdminNotificationListAPI.as_view(), name='admin_main_notification_list'),
    path('soft_delete/', soft_delete, name='soft_delete'),
    path('translate/', translate, name='translate'),
    path('soft_delete_exhibition/', soft_delete_exhibition, name='soft_delete_exhibition')

]