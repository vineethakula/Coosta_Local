from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset, password_reset_confirm

from coosta_users.models import UserProfile, NonPreApprovedUser, \
    PreApprovedDocuments, PreApprovedUser, Documents
from coosta_users.serializers import UserProfileSerializer, GroupSerializer, \
    UserSerializer, GetNonPreApprovedUserSerializer, \
    PostNonPreApprovedUserSerializer, GetPreApprovedDocumentsSerializer, \
    PostPreApprovedDocumentsSerializer, PostPreApprovedUserSerializer, GetPreApprovedUserSerializer, \
    DocumentsSerializer
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.hmac.views import RegistrationView as RegView
from rest_framework.permissions import IsAuthenticated
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from rest_framework.parsers import MultiPartParser, FormParser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'email', 'first_name', 'last_name',
                     'is_staff', 'is_active', 'is_superuser', 'date_joined',
                     'groups',)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users profile to be viewed or edited.
    """
    # parser_classes = (FileUploadParser,)
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('area_code', 'mobile_number', 'address', 'city', 'town',
                     'state', 'zip_code',)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def put(self, request):
        serializer = self.get_serializer(data=request.DATA,
                                         files=request.FILES)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RegistrationView(RegView):
    """
    API endpoint for Registration view.
    This only overrides the Registration form, other functionality remains
    same as the base class
    """
    form_class = RegistrationFormUniqueEmail


@login_required(login_url='/user/login/?next=/user/account_settings/')
@csrf_exempt
def account_settings(request):
    if request.method == 'POST':
        u = User.objects.get(username__exact=request.user.username)
        if 'c_password' in request.POST:
            if not u.check_password(request.POST.get('c_password')):
                return render(
                    request,
                    'user/acc_settings.html',
                    {'error': "current password not matched"}
                )
            else:
                try:
                    u.set_password(request.POST.get('new_password1'))
                    u.save()
                    return HttpResponseRedirect('/user/login/?next=/')
                except:
                    return render(
                        request,
                        'user/acc_settings.html',
                        {'error': "please use proper password"}
                    )

        if 'e_password' in request.POST:
            if not u.check_password(request.POST.get('e_password')):
                return render(
                    request,
                    'user/acc_settings.html',
                    {'error': "Incorrect Password"}
                )
            else:
                try:
                    u.is_active = 0
                    u.save()
                    auth.logout(request)
                    return render(request, 'user/acc_delete_confirm.html')
                except Exception as e:
                    return render(
                        request,
                        'user/acc_settings.html',
                        {'error': e}
                    )

    return render(request, 'user/acc_settings.html')


@csrf_exempt
def account_delete_confirm(request):
    return render(request, 'user/acc_delete_confirm.html')


@login_required(login_url='/user/login/')
@csrf_exempt
def profile_settings(request):
    #TODO convert the logic of profile creation from pythonic to api based
    try:
        UserProfile.objects.get(user=request.user)
    except:
        user_profile = UserProfile()
        user_profile.user = request.user
        user_profile.save()
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.profile_image = request.FILES['profile_image']
        user_profile.save()
    return render(request, 'user/profile_sett.html')


def reset_confirm(request, uidb36=None, token=None):
    template = password_reset_confirm(request,
                                      template_name='app/reset_confirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('app:login'))
    return template


def reset(request):
    template = password_reset(request, template_name='app/reset.html',
                               email_template_name='app/reset_email.html',
                               subject_template_name='app/reset_subject.txt',
                               post_reset_redirect=reverse('app:login'))
    return template


class NonPreApprovedUserViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows All Non Pre Approved Users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = NonPreApprovedUser.objects.all().order_by('-created_on')
    serializer_class = GetNonPreApprovedUserSerializer
    custom_serializer_classes = {
        'create': PostNonPreApprovedUserSerializer,
        'update': PostNonPreApprovedUserSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = {
        'user__id': ['exact']
    }


class PreApprovedUserViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows All Pre Approved Users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = PreApprovedUser.objects.all().order_by('-created_on')
    serializer_class = GetPreApprovedUserSerializer
    custom_serializer_classes = {
        'create': PostPreApprovedUserSerializer,
        'update': PostPreApprovedUserSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
        'user__id': ['exact']
    }


class DocumentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows All Documents to be viewed or edited.
    """
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(file=self.request.data.get('file'))


class PreApprovedDocumentsViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows Adding, Editing and Viewing the 
    PreApprovedDocuments.
    """
    permission_classes = (IsAuthenticated,)
    queryset = PreApprovedDocuments.objects.all()

    serializer_class = GetPreApprovedDocumentsSerializer

    custom_serializer_classes = dict.fromkeys(
        ['create', 'update'],
        PostPreApprovedDocumentsSerializer
    )
