from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'name', 'summary', 'submission_type', 'submission_url', 'submission_file']
        read_only_fields = ['id']
