from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Course, Resource, Question, Answer

ROLE_CHOICES = (
    ('student', 'Student'),
    ('mentor', 'Mentor'),
)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")
    email = forms.EmailField(max_length=254, required=True, label="Email Address")
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="Role"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class ResourceForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=200,
        required=False,
        help_text='Enter comma-separated tags (e.g., Chapter 1, Mid-term, Video).',
        widget=forms.TextInput(attrs={'placeholder': 'e.g., notes, exam-prep, python'})
    )

    class Meta:
        model = Resource
        fields = ['title', 'description', 'file', 'tags']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add an optional description...'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Search...'})
    )

# Forms for the new Q&A feature
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your question title'}),
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Provide more details about your question...'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your answer...'}),
        }
        labels = {
            'content': '', # Hides the label for a cleaner UI in the template
        }

