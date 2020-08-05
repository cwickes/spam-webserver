from django.views import generic
from identifier.models import ReportedMessage

class ReportedMessageView(generic.ListView):
	model = ReportedMessage
	paginate_by = 15

class ReviewMessageView(generic.DetailView):
	model = ReportedMessage