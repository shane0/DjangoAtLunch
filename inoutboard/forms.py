from django import forms

class StaffForm(forms.Form):
    status = forms.BooleanField(required=False)
    message = forms.CharField(required=False)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
