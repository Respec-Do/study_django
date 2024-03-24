from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django_visit_count.mixins import VisitCountMixin

from main.models import VisitRecord

class CustomVisitCountMixin(VisitCountMixin):
    def increment_count(self, request):
        super().count_visit(request)

        visit_record, created = VisitRecord.objects.get_or_create(date=timezone.now().date())

        if created:
            visit_record.count = 1
        else:
            visit_record.count+= 1
        visit_record.save()
class MainView(CustomVisitCountMixin, View):
    def get(self, request):
        try:
            member = request.session['member']
        except KeyError:
            member = None

        visit_record, created = VisitRecord.objects.get_or_create(date=timezone.now().date())
        if created:
            visit_record.count = 1
        else:
            visit_record.count+= 1
        visit_record.save()

        return render(request, 'main.html', {'member': member})

    # return render(request, main:html)


