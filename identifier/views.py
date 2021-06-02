from django.views import generic
from identifier.models import ReportedMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from identifier.forms import ReviewForm
from rest_framework.views import APIView
from rest_framework import authentication
from identifier.serializers import SafetySerializer
from rest_framework.response import Response
from django.http import Http404

class ReportedMessageView(LoginRequiredMixin, generic.ListView):
	model = ReportedMessage
	paginate_by = 15

class ReviewMessageView(LoginRequiredMixin, UpdateView):
	model = ReportedMessage
	fields = ['is_safe']

	def get_success_url(self):
		return '/identifier/'

class ReportMessage(APIView):
	# Require auth token to report/check message
	authentication_classes = [authentication.TokenAuthentication]

	def get_report(self, msg):
		try:
			# Perform search operation to find similar message
			#return ReportedMessage.objects.get(message_body__search=msg)
			return ReportedMessage.objects.get(message_body__icontains=msg)
		except ReportedMessage.DoesNotExist:
			# When message cannot be found, create new entry and return
			print("MESSAGE NOT FOUND\n")
			raise Http404

	def get(self, request, format=None):
		msg = request.GET.get('msg')
		report = self.get_report(msg)
		serializer = SafetySerializer(report)
		return Response(serializer.data)