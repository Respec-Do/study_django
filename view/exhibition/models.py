from django.db import models

from exhibition.managers import ExhibitionManager
from file.models import File
from like.models import Like
from school.models import School
from view.models import Period


class Exhibition(Period):
    exhibition_title = models.CharField(null=False, max_length=40)
    exhibition_content = models.CharField(null=False, max_length=1000)
    # False=관리자, True=school
    exhibition_status = models.BooleanField(null=False, blank=False, default=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    exhibition_post_status = models.BooleanField(null=False, default=True)
    exhibition_url = models.TextField(null=False, blank=False)
    exhibition_view_count = models.IntegerField(null=False, blank=False, default=0)
    objects = models.Manager()
    enabled_objects = ExhibitionManager()

    class Meta:
        db_table = 'tbl_exhibition'
        ordering = ['-id']

    def get_absolute_url(self):
        return f'/exhibition/detail/?id={self.id}'

class ExhibitionFile(Period):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.PROTECT, null=False)
    file = models.ForeignKey(File, primary_key=True, on_delete=models.PROTECT, null=False)
    path = models.ImageField(null=False, blank=False, upload_to='exhibition/%Y/%m/%d')
    download_path = models.ImageField(null=False, blank=False, upload_to='exhibition_down/%Y/%m/%d')
    preview = models.BooleanField(default=False)
    class Meta:
        db_table = 'tbl_exhibition_file'

class ExhibitionLike(Period):
    like = models.ForeignKey(Like, primary_key=True, on_delete=models.PROTECT, null=False)
    class Meta:
        db_table = 'tbl_exhibition_like'