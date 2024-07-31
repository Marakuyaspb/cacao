from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import Answer, Gift, GiftCat



@admin.register(GiftCat)
class GiftCatAdmin(admin.ModelAdmin):
	list_display = ['id', 'gifts_cat']
	list_filter = ['gifts_cat']


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
	list_display = ['id', 'gifts_cat', 'gift', 'price']
	list_filter = ['gift']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'result_quantity', 'result_price', 'result_budget', 'gift', 'created']
	list_filter = ['gift']