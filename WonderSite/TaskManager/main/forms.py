from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "date", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назначте дедлайн в формате (Пример: 2022-12-11 15:45:26)',
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),

        }
