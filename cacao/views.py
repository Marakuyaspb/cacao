from django.shortcuts import render

def quiz(request):
	return render(request, 'cacao/quiz.html')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# from .bot import bot

# @method_decorator(csrf_exempt, name='dispatch')
# class TelegramWebhook(View):
#    def post(self, request):
#        json_str = request.body.decode('UTF-8')
#        update = telebot.types.Update.de_json(json_str)
#        bot.process_new_updates([update])
#        return JsonResponse({'status': 'ok'})
   
