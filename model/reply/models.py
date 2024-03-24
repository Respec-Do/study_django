from django.db import models
from model.models import Period
from member.models import Member
from post.models import Post

class Reply(Period):
    PRIVATE_STATUS = [
        (True, '비밀 댓글'),
        (False, '일반 대글')
    ]

    reply_content = models.TextField(null=False, blank=False)
    member = models.ForeignKey(Member, null=False, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, null=False, on_delete=models.PROTECT)
    group_id = models.BigIntegerField(null=True)
    reply_private_status = models.BooleanField(null=False, default=False, choices=PRIVATE_STATUS)
    # True면 비밀 댓글, False면 일반 댓글
    reply_depth = models.BigIntegerField(null=False, default=1)

    class Meta:
        db_table = 'tbl_reply'
        ordering = ['-id']

    def __str__(self):
        return self.reply_content