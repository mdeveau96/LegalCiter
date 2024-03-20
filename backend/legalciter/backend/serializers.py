from rest_framework import serializers
from backend.models import Case, Cite


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['case_id', 'title', 'pub_date', 'case_text']


class CiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cite
        fields = ['cite_id', 'title', 'cite_text']
