from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_ta = models.TextField(blank=True, null=True)
    question_te = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_ta = RichTextField(blank=True, null=True)
    answer_te = RichTextField(blank=True, null=True)

    def translate_text(self, text, lang):
        translator = Translator()
        try:
            translation = translator.translate(text, dest=lang)
            return translation.text
        except:
            return text

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_ta:
            self.question_ta = self.translate_text(self.question, 'ta')
        if not self.question_te:
            self.question_te = self.translate_text(self.question, 'te')
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.answer_ta:
            self.answer_ta = self.translate_text(self.answer, 'ta')
        if not self.answer_te:
            self.answer_te = self.translate_text(self.answer, 'te')
        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):
        return self.question
