from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cv', 'cover_letter']

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        self.fields['cv'].label = 'Upload Your CV'
        self.fields['cover_letter'].label = 'Write Your Cover Letter'
