#User Registration Form
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class AccountSettingsForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(required=True, max_length=30, render_value=False)
        ),
        label=_('Current Password'))

    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(required=True, max_length=30, render_value=False)
        ),
        label=_('New Password')
    )

    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(required=True, max_length=30, render_value=False)
        ),
        label=_('Confirm New Password')
    )

    def validate_passwords(self):
        if self.cleaned_data['current_password'] != User.password:
            raise forms.ValidationError(_("Current password doesn't match"))

        if 'new_password' in self.cleaned_data and \
                        'confirm_new_password' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    _("The two password fields did not match.")
                )


class ProfileSettingsForm(forms.Form):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField(
        widget=forms.TextInput(), label=_("Email address"))
    area_code = forms.TextInput()
    number = forms.TextInput()
    address = forms.TextInput()
    city = forms.TextInput()
    state = forms.TextInput()
    zip = forms.TextInput()


    def validation(self):
        pass
    #all sort of validation here