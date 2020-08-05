from django.db import models
from django.contrib.auth.models import User

class ReportedMessage(models.Model):
	sender = models.EmailField()
	message_body = models.TextField()
	report_date = models.DateTimeField(auto_now_add=True)
	review_date = models.DateTimeField(null=True)
	reviewed_by = models.ForeignKey(User, models.PROTECT, null=True)
	is_safe = models.BooleanField(null=True)