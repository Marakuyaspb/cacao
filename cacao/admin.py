from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import Answer, Present, PresentCat



@admin.register(PresentCat)
class PresentCatAdmin(admin.ModelAdmin):
	list_display = ['id', 'presents_cat']
	list_filter = ['present']


@admin.register(Present)
class PresentAdmin(admin.ModelAdmin):
	list_display = ['id', 'presents_cat', 'present', 'price']
	list_filter = ['present']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'result_quantity', 'result_price', 'result_budget', 'present', 'created']
	list_filter = ['present']