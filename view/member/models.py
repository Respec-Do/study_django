from django.db import models

from member.managers import MemberManager
from view.models import Period


class Member(models.Model):
    member_email = models.TextField(null=False, blank=False)
    member_password = models.TextField(null=False, blank=False)
    member_name = models.TextField(null=False, blank=False)
    member_school_email = models.CharField(blank=False, max_length=50, default="<EMAIL>")
    member_phone = models.CharField(blank=False, max_length=30)
    # 추가
    member_status = models.BooleanField(null=False, default=True)
    # 탈퇴회원 구분
    member_is_active = models.BooleanField(null=False, default=True)
    # 학교회원 구분
    member_is_school = models.BooleanField(null=False, default=False)

    objects = models.Manager()
    enabled_objects = MemberManager()

    class Meta:
        db_table = 'tbl_member'
