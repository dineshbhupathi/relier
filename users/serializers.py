from rest_framework.serializers import HyperlinkedModelSerializer,HyperlinkedIdentityField
from django.contrib.auth.models import User

class UserSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='User', lookup_field='id')
    class Meta:
        model = User
        fields = ["url","id","username","email"]