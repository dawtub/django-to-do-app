from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.auto_id = False

    class Meta:
        model = Task
        exclude = ['time', 'completed']
        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-control',
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'What u want to do?',
            })
        }
        labels={
            'user': '',
            'text': '',
        }
