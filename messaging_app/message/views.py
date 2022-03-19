from rest_framework.views import APIView
from rest_framework.response import Response

from message.models import Message
from message.serializers import MessageSerializer
from django.http import JsonResponse

class ReceiveMessages(APIView):
    def get(self, request, recipient):
        messages = Message.objects.filter(recipient = recipient)
        serializer = MessageSerializer(messages, many = True)
        return Response(serializer.data)

class SendMessage(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.query_params)
        serializer.is_valid()
        serializer.save()
        print(serializer)
        return Response(request.query_params)
