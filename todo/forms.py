from django import forms
from .models import TodoItem


class AddTodo(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["title", "description"]
