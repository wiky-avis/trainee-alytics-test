
from django import forms
from django.contrib.auth import get_user_model

from .models import Function

User = get_user_model()


class FunctionForm(forms.ModelForm):
    class Meta:
        model = Function
        fields = ['function', 'interval', 'dt']
