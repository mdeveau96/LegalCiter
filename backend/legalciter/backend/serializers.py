from rest_framework import serializers
from backend.models import Case, Cite, CustomUser


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['title', 'pub_date', 'case_text']


class CiteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Cite
        fields = ['name', 'cite_text', 'owner']


class UserSerializer(serializers.ModelSerializer):
    cases = serializers.PrimaryKeyRelatedField(many=True, queryset=Case.objects.all())
    cites = serializers.PrimaryKeyRelatedField(many=True, queryset=Cite.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'cites']