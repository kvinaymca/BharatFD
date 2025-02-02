from django.contrib import admin
from .models import FAQ
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'question_hi', 'question_ta', 'question_te', 'answer_hi', 'answer_ta', 'answer_te')
    search_fields = ('question', 'answer')
    list_filter = ('question', 'answer')
    fieldsets = (
        ('English', {
            'fields': ('question', 'answer')
        }),
        ('Hindi', {
            'fields': ('question_hi', 'answer_hi')
        }),
        ('Tamil', {
            'fields': ('question_ta', 'answer_ta')
        }),
        ('Telugu', {
            'fields': ('question_te', 'answer_te')
        }),
    )