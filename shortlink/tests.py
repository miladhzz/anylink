from django.test import TestCase
from .models import Link


class LinkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Link.objects.create(completelink='djagolearn.ir')

    def test_completelink_content(self):
        link = Link.objects.get(pk=1)
        expected_completelink = 'djagolearn.ir'
        self.assertEqual(expected_completelink, link.completelink)

    def test_unique_link(self):
        Link.objects.create(completelink='djagolearn.ir')
