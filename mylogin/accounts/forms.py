# students/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter valid email address'
            }),
            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'BSIT, BSCrim, BSBA, etc.'
            }),
        }

    # Custom Validation for name
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    # Custom Validation for course
    def clean_course(self):
        course = self.cleaned_data.get('course').upper()
        allowed_courses = ['BSIT', 'BSCRIM', 'BSBA']
        if course not in allowed_courses:
            raise forms.ValidationError("Course must be BSIT, BSCrim, or BSBA.")
        return course