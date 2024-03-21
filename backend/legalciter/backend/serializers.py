from rest_framework import serializers
from backend.models import Case, Cite, CustomUser


class CaseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Case
        fields = ['url', 'id', 'title', 'pub_date', 'case_text']


class CiteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Cite
        fields = ['url', 'id', 'name', 'cite_text', 'owner']


class UserSerializer(serializers.ModelSerializer):
    cites = serializers.HyperlinkedRelatedField(many=True, view_name='cite-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'email', 'cites']