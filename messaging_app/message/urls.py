from django.urls import path
from message.views import ReceiveMessages, SendMessage

urlpatterns = [
  path('messages/<recipient>', ReceiveMessages.as_view()),
  path('send_message', SendMessage.as_view())
]
