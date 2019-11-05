from django.contrib.auth.models import User, Group
from rest_framework import serializers
from coosta_users.models import UserProfile, NonPreApprovedUser, PreApprovedDocuments, PreApprovedUser, Documents
from django.core.exceptions import ValidationError


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('user', 'url', 'area_code', 'mobile_number', 'address',
                  'city', 'town', 'state', 'zip_code', 'profile_image')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'is_superuser', 'date_joined',
                  'groups', 'userprofile')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GetNonPreApprovedUserSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = NonPreApprovedUser
        fields = ('id', 'user', 'created_on')


class PostNonPreApprovedUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NonPreApprovedUser
        fields = ('id', 'user')


class DocumentsSerializer(serializers.HyperlinkedModelSerializer):

    file = serializers.FileField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Documents
        fields = ('url', 'id', 'file')


class GetPreApprovedUserSerializer(serializers.HyperlinkedModelSerializer):

    documents = DocumentsSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = PreApprovedUser
        fields = ('id', 'user', 'documents', 'created_on')


class PostPreApprovedUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PreApprovedUser
        fields = ('id', 'user', 'documents', 'created_on')


class GetPreApprovedDocumentsSerializer(serializers.HyperlinkedModelSerializer):

    file = DocumentsSerializer(read_only=True, required=False)
    pre_approved_user = GetPreApprovedUserSerializer()

    class Meta:
        model = PreApprovedDocuments
        fields = ('id', 'pre_approved_user', 'file')


class PostPreApprovedDocumentsSerializer(serializers.HyperlinkedModelSerializer):
    pre_approved_user = PostPreApprovedUserSerializer()

    class Meta:
        model = PreApprovedDocuments
        fields = ('id', 'pre_approved_user', 'file')

    def create(self, validated_data):
        pre_approved_user = PreApprovedUser.objects.filter(
            user=validated_data['pre_approved_user']['user'])
        if pre_approved_user:
            pre_approved_documents = PreApprovedDocuments.objects.create(
                pre_approved_user=pre_approved_user[0],
                file=validated_data['file'])
            return pre_approved_documents
        else:
            raise ValidationError("Pre Approved user doesn't exist")