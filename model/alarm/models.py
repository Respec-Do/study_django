from django.db import models

from alarm.managers import AlarmManager
from member.models import Member
from model.models import Period
from post.models import Post


class Alarm(Period):
    receiver = models.ForeignKey(Member, null=False, related_name='receiver', on_delete=models.PROTECT)
    sender = models.ForeignKey(Member, null=False,  related_name='sender', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, null=False, on_delete=models.PROTECT)
    # 0 : 안 읽음 1 : 읽음 -1 삭제
    status = models.SmallIntegerField(default=0)
    # managers 로 지정된 함수를 따로 만들때 사용하는 방법
    objects = models.Manager()
    enabled_objects = AlarmManager()

    class Meta:
        db_table = 'tbl_alarm'
        ordering = ['-id']