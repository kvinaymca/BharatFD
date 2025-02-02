from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQList(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        faqs = FAQ.objects.all()
        for faq in faqs:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)
        return faqs

class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_object(self):
        obj = super().get_object()
        lang = self.request.query_params.get('lang', 'en')
        obj.question = obj.get_translated_question(lang)
        obj.answer = obj.get_translated_answer(lang)
        return obj