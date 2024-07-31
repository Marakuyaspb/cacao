from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static

#from telegrambot.decorators import command, regex
#from telegrambot.views import StartView, AuthorCommandView, AuthorInverseListView, AuthorCommandQueryView, UnknownView, AuthorName

from . import views



app_name = 'cacao'

urlpatterns = [
    path('', views.quiz, name = 'quiz'),

    # command('start', StartView.as_command_view()),
    # command('author', AuthorCommandView.as_command_view()),
    # command('author_inverse', AuthorInverseListView.as_command_view()),
    # command('author_query', login_required(AuthorCommandQueryView.as_command_view())),
    # unknown_command(UnknownView.as_command_view()),
    #        regex(r'author_(?P<name>\w+)', AuthorName.as_command_view()),
]