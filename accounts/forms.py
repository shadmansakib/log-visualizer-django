from django.contrib.auth.forms import PasswordChangeForm

# class CustomPasswordChangeForm(PasswordChangeForm):
from django.views.generic.edit import FormMixin


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Old password',
        })

        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'New password',
        })

        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm New Password',
        })
