from django.db import models
from django.utils import timezone


class EnableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)


class Period(models.Model):
    created_date = models.DateTimeField(null=False, auto_now_add=True)
    # default 파라미터에 전달할때는 함수형태로 전달이 가능. -> () 안붙이고 쓰기
    updated_date = models.DateTimeField(null=False, default=timezone.now)
    # 역참조 시 위에 선언한 Manager가 사용된다.
    objects = models.Manager()
    enabled_objects = EnableManager()

    class Meta:
        abstract = True

