from rest_framework import serializers
from identifier.models import ReportedMessage

# used for GET requests to display safety information
class SafetySerializer(serializers.Serializer):
	report_date = serializers.DateTimeField()
	review_date = serializers.DateTimeField()
	is_safe = serializers.BooleanField()

# used to insert new ReportedMessage objects
class ReportSerializer(serializers.Serializer):
	sender = serializers.EmailField()
	message_body = serializers.CharField()
	report_date = serializers.DateTimeField()

	def create(self, validated_data):
		return ReportedMessage.objects.create(**validated_data)