from django import forms

class ReviewForm(forms.Form):
	safe = forms.NullBooleanField(
		widget=forms.RadioSelect(
			choices=[
				(True, 'Message is safe'),
				(False, 'Message is NOT safe'),
			]
		)
	)
