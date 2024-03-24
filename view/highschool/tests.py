from django.test import TestCase

from member.models import Member
from highschool.models import HighSchool

class HighschoolTestCase(TestCase):
    member = Member.objects.get(id=7)
    data = {
        'member': member,
    }

    highschool = HighSchool(**data)
    highschool.save()
