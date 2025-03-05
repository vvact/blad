from django import forms
from django.contrib.auth.forms import SetPasswordForm

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize field labels and help texts if you want
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password2'].label = 'Confirm New Password'

        # Add custom placeholders (optional)
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'Enter your new password'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirm your new password'})

    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')

        # Example of a custom password rule
        if 'password' in password.lower():
            raise forms.ValidationError("Your password can't contain the word 'password'.")
        
        return password
