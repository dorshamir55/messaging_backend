from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from message.models import Message
from message.serializers import MessageSerializer

client = Client()

class GetAllMessagesByRecipientTest(TestCase):
    def setUp(self):
        Message.objects.create(sender='Dor', recipient='Keren', message='Hi Keren, how are you today? :)')

    def test_get_messages_by_recipient(self):
        response = client.get(reverse('receive_message', args=('Keren',)))
        messages = Message.objects.filter(recipient='Keren')
        serializer = MessageSerializer(messages, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_messages_by_recipient_no_result(self):
        response = client.get(reverse('receive_message', args=('David',)))
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SendMessageTests(TestCase):
    def test_send_valid_message(self):
        self.assertEqual(len(Message.objects.all()), 0)
        response = client.post('http://localhost/api/send_message?sender=Dor&recipient=Keren&message=Nice to learn about Tikal!')
        self.assertEqual(len(Message.objects.all()), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
