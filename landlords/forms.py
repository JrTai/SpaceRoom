from django import forms

class MessageForm(forms.Form):
	potential_tenant = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=20, required=False, label='E-mail')
	content = forms.CharField(max_length=200, widget=forms.Textarea())

	def clean_content(self):
		content = self.cleaned_data['content']
		if len(content) < 5:
			raise forms.ValidationError('Not enough words')
		return content