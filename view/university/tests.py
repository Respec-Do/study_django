from django.test import TestCase

from member.models import Member
from university.models import University


class UniversityTests(TestCase):
    member = Member.objects.get(id=6)
    data = {
        'university_member_school' : '서울대학교',
        'university_member_major' : '경제학과',
        'member' : member
    }

    university = University(**data)
    university.save()