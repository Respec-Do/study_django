import json
from datetime import timedelta

from django.db import transaction
from django.db.models import F, Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django_visit_count.mixins import VisitCountMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from exhibition.models import Exhibition
from main.models import VisitRecord
from member.models import Member
from member.serializers import MemberSerializer
from notification.models import Notification, NotificationFile


class MemberJoinView(View):

    def get(self, request):
        return render(request, 'member/join.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_email': data['member-email'],
            'member_password': data['member-password'],
            'member_name': data['member-name']
        }

        Member.objects.create(**data)

        return redirect('member:login')


class MemberLoginView(View):

    def get(self, request):
        return render(request, 'member/login.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_email': data['member-email'],
            'member_password': data['member-password']
        }

        # exists() 를 사용하기 위해서 QuerySet 객체로 조회
        member = Member.objects.filter(**data)
        url = 'member:login'
        if member.exists():
            # 성공
            request.session['member'] = MemberSerializer(member.first()).data
            # '/' root라고 말함.
            url = '/'
        # 일괄처리한 것임.
        return redirect(url)

class MemberLogoutView(View):
     def get(self, request):
         request.session.clear()
         return redirect('member:login')



class AdminMemberLoginView(View):
    def get(self, request):
        return render(request, 'admin/login.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_email': data['member-email'],
            'member_password': data['member-password'],
        }

        # exists() 를 사용하기 위해서 QuerySet 객체로 조회
        member = Member.objects.filter(**data)
        url = 'member:admin_login'
        if member.exists():
            # 성공
            return redirect('member:admin_main')
        # 일괄처리한 것임.
        return redirect(url)


class AdminMainView(View):
    def get(self, request):
        today = timezone.now().date()
        seven_days_ago = today - timedelta(days=6)
        visit_records = VisitRecord.objects.filter(date__range=[seven_days_ago, today])
        today_records = VisitRecord.objects.get(date = today)

        visit_records_total = VisitRecord.objects.filter(date__range=[seven_days_ago, today]).aggregate(total=Sum('count'))
        total_count = visit_records_total['total'] if visit_records_total['total'] is not None else 0

        # 각 visit_records의 date 필드를 문자열로 변환하여 직렬화
        visit_records_data = [{'date': record.date.strftime('%Y-%m-%d'), 'count': record.count} for record in
                              visit_records]
        visit_records_json = json.dumps(visit_records_data)

        context = {
            'visit_records_json': visit_records_json,
            'today_records': today_records,
            'visit_records_total': total_count
        }

        return render(request, 'admin/main.html', context)


class AdminMainUserView(View):
    def get(self, request):
        return render(request, 'admin/main_user.html')



class AdminMainUserListAPI(APIView):
    def get(self, request, page):
        row_count = 5
        offset = (page -1) * row_count
        limit = page * row_count

        columns = [
            'id',
            'member_email',
            'member_name',
            'member_phone',

        ]

        members = Member.enabled_objects.values(*columns)[offset:limit]
        total_count = Member.enabled_objects.count()
        member_info = {
            'members' : members,
            'total_count' : total_count
        }

        return Response(member_info)




class AdminMainNotificationView(View):
    def get(self, request):
        return render(request, 'admin/main_notification.html')

class AdminNotificationListAPI(APIView):
    def get(self, request, page):
        row_count = 5
        offset = (page - 1) * row_count
        limit = page * row_count

        columns = [
            'id',
            'notification_title',
            'notification_status',
            'created_date',
            'notification_view_count'
        ]

        option = request.GET.get('option')

        if option == '커뮤니티':
            notifications = Notification.enabled_objects.filter(notification_status=0).values(*columns)[offset:limit]
            total_count = Notification.enabled_objects.filter(notification_status=0).count()
        elif option == '원랩':
            notifications = Notification.enabled_objects.filter(notification_status=1).values(*columns)[offset:limit]
            total_count = Notification.enabled_objects.filter(notification_status=1).count()
        elif option == '장소공유':
            notifications = Notification.enabled_objects.filter(notification_status=2).values(*columns)[offset:limit]
            total_count = Notification.enabled_objects.filter(notification_status=2).count()
        elif option == '공모전':
            notifications = Notification.enabled_objects.filter(notification_status=3).values(*columns)[offset:limit]
            total_count = Notification.enabled_objects.filter(notification_status=3).count()
        else:
            notifications = Notification.enabled_objects.values(*columns)[offset:limit]
            total_count = Notification.enabled_objects.count()



        notification_info= {
            'notifications' : notifications,
            'total_count' : total_count
        }

        return Response(notification_info)

def soft_delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_items = data.get("selected_items")
        print(selected_items)
        # 선택된 항목들의 상태를 0으로 변경하는 코드 작성
        for item_id in selected_items:
            try:
                Notification.objects.filter(id=item_id).update(notification_post_status=False)

            except Notification.DoesNotExist:
                pass  # 항목이 존재하지 않는 경우 무시

        return JsonResponse({'message': '선택된 항목이 성공적으로 삭제되었습니다.'})

    return JsonResponse({'error': 'POST 요청이 필요합니다.'}, status=400)

def translate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_items = data.get("selected_items")
        print(selected_items)
        # 선택된 항목들의 상태를 0으로 변경하는 코드 작성
        for item_id in selected_items:
            try:
                Member.objects.filter(id=item_id).update(member_is_school=True)

            except Member.DoesNotExist:
                pass  # 항목이 존재하지 않는 경우 무시

        return JsonResponse({'message': '선택된 항목이 성공적으로 삭제되었습니다.'})

    return JsonResponse({'error': 'POST 요청이 필요합니다.'}, status=400)

def soft_delete_exhibition(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_items = data.get("selected_items")
        print(selected_items)
        # 선택된 항목들의 상태를 0으로 변경하는 코드 작성
        for item_id in selected_items:
            try:
                Exhibition.objects.filter(id=item_id).update(exhibition_post_status=False)

            except Exhibition.DoesNotExist:
                pass  # 항목이 존재하지 않는 경우 무시

        return JsonResponse({'message': '선택된 항목이 성공적으로 삭제되었습니다.'})

    return JsonResponse({'error': 'POST 요청이 필요합니다.'}, status=400)


class AdminMainNotificationWriteView(View):
    def get(self, request):
        return render(request, 'admin/../templates/notification/write.html')

class AdminMainInquiryView(View):
    def get(self, request):
        return render(request, 'admin/main_inquiry.html')

class AdminMainPaymentView(View):
    def get(self, request):
        return render(request, 'admin/main_payment.html')

class AdminMainExhibitionView(View):
    def get(self, request):
        return render(request, 'admin/main_exhibition.html')


class AdminMainExhibitionListAPI(APIView):
    def get(self, request, page):
        row_count = 5
        offset = (page -1) * row_count
        limit = page * row_count

        columns = [
            'id',
            'exhibition_title',
            'exhibition_view_count',
            'school__member__member_name',
            'created_date'
        ]

        exhibitions = Exhibition.enabled_objects\
                          .annotate(school_member_name=F('school__member__member_name')).values(*columns)[offset:limit]
        total_count = Exhibition.enabled_objects.count()
        exhibition_info = {
            'exhibitions' : exhibitions,
            'total_count' : total_count
        }

        return Response(exhibition_info)

