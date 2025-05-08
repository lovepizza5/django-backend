from rest_framework import serializers
from .models import ContactSubmission

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'
