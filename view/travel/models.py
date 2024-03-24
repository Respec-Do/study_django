from django.db import models

class Travel(models.Model):
    travel_budget = models.BigIntegerField(null=False, default=0)
    travel_destination = models.TextField(null=False, blank=False)
    travel_date = models.TextField(null=False, blank=False)
    # False = 예약 안함, True = 예약 함.
    travel_hotel_reservation = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'tbl_travel'

    def get_absolute_url(self):
        return f'/travel/detail/?id={self.id}'