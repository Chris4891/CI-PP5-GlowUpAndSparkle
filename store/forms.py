from store.models.newsletter import Subscriber
from django import forms
class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']