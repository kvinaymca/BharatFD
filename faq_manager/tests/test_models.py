import pytest
from django.test import TestCase
from faq_manager.models import FAQ
pytestmark = pytest.mark.django_db
class FAQModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faq = FAQ.objects.create(
            question='What is Django?',
            answer='A Python web framework.'
        )
    def test_translations_are_created(self):
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)
    def test_translate_text_method(self):
        translation = self.faq.translate_text('hi')
        self.assertIn('question', translation)
        self.assertIn('answer', translation)