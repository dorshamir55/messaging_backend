from django.urls import path
from message.views import receive_message, send_message

urlpatterns = [
  path('messages/<recipient>', receive_message.as_view(), name='receive_message'),
  path('send_message', send_message.as_view(), name='send_message')
]
