from django.test import TestCase

from member.models import Member
from school.models import School


class SchoolTests(TestCase):
    school = School.objects.create(
        member = Member.objects.get(id=8)
    )