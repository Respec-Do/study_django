from django.db import models

from view.models import Period


class File(Period):
    file_size = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'tbl_file'
        ordering = ['-id']