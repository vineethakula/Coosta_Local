from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import filters
from rest_framework.permissions import AllowAny
from django.db.models import Q
from drf_custom_viewsets.viewsets import CustomSerializerViewSet

# Create your views here.


class CoostaMessageViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows Property to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = Coosta_Message.objects.all()
    serializer_class = GetCoostaMessageSerializer
    custom_serializer_classes = {
        'create': PostCoostaMessageSerializer,
        'update': PostCoostaMessageSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('create_on', 'read_by_recipient', 'property')
    filter_fields = {
            'sender': ['exact'],
            'recipient': ['exact'],
            'id': ['exact'],
        }


@login_required(login_url='/user/login/')
def contact_owner(request):
    return render(request, 'message/contact_owner.html')

@login_required(login_url='/user/login/')
def message_box(request, sender_id=None):
    if sender_id == None:
        message_users_temp = []
        message_users = []
        messages = Coosta_Message.objects.filter(Q(recipient=request.user)).order_by('-id')
        for message in messages:
            if message.sender:
                if not message.sender in message_users_temp:
                    m_obj = {'sender': message.sender, 'latest': message.message_body}
                    message_users_temp.append(message.sender)
                    message_users.append(m_obj)
            else:
                m_obj = {'sender': message.sender, 'latest': message.message_body}
                message_users_temp.append(message.sender)
                message_users.append(m_obj)

        return render(request, 'message/message_box.html', {'message_users': message_users})
    else:
        sender = User.objects.get(id=sender_id)
        message_conversation = Coosta_Message.objects.filter(Q(recipient=request.user, sender=sender) |
                                                             Q(recipient=sender, sender=request.user)).order_by(
            'create_on')
        return render(request, 'message/message_detail.html', {'message_conversation': message_conversation,
                                                               'sender_id': sender_id, 'sender': sender})
