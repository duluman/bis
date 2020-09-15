from django import forms
from users.models import MyUser, Profile, RoNewsletter
from django.contrib.auth import password_validation


class RoNewsletterForm(forms.Form):
    email = forms.EmailField(required=True, label='Adresa ta de email')

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def save(self):

        email = self.cleaned_data['email']
        user_email = RoNewsletter()
        user_email.email = email
        user_email.save()


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(
        required=True,
        max_length=255,
        label='Parola',
        widget=forms.PasswordInput,)


class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=255, label='Prenume')
    last_name = forms.CharField(required=True, max_length=255, label='Nume')
    email = forms.EmailField(required=True, label='E-mail')

    password = forms.CharField(
        required=True,
        max_length=255,
        label='Parola',
        widget=forms.PasswordInput,
    )
    password_confirm = forms.CharField(
        required=True,
        max_length=255,
        label='Confirma parola',
        widget=forms.PasswordInput,
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        users = MyUser.objects.filter(email=email)

        if users.count() != 0:
            raise forms.ValidationError('E-mail-ul exista in baza de date')

        return email

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password_confirm != password:
            raise forms.ValidationError("Password confirm doesn't match")

        return password_confirm

    def save(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = MyUser.objects.create_user(email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()


class UploadFileForm(forms.Form):
    my_file = forms.FileField(required=True)


class UploadProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


class SetPassword(forms.Form):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html())
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_validation.validate_password(password, self.user)
        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError('Password mismatch')

        return password_confirmation

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        self.user.set_password(password)

        if commit:
            self.user.save()

        return self.user


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=255, label='Nume')
    last_name = forms.CharField(required=True, max_length=255, label='Prenume')
    email = forms.EmailField(required=True, label='E-mail')
    mobile = forms.CharField(required=False, max_length=20, label='Numar de telefon')
    subject = forms.CharField(required=True, max_length=255, label='Subiect')
    message = forms.CharField(required=True, min_length=10, max_length=1000, label='Mesajul tau', widget=forms.Textarea)
    gdpr = forms.BooleanField(required=True, label='Sunt de acord ca datele mele să fie stocate în conformitate cu Politica de confidențialitate')


class EnContactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)
    email = forms.EmailField(required=True)
    mobile = forms.CharField(required=False, max_length=20)
    subject = forms.CharField(required=True, max_length=255)
    message = forms.CharField(required=True, min_length=10, max_length=1000, widget=forms.Textarea)
    gdpr = forms.BooleanField(required=True,
                              label='I agree with General Data Protection Regulation')



# class ChangePasswordForm(forms.Form):
#     password = forms.CharField(
#         required=True,
#         max_length=255,
#         label='Current Password',
#         widget=forms.PasswordInput)
#
#     new_password = forms.CharField(
#         required=True,
#         max_length=23,
#         label='New Password',
#         widget=forms.PasswordInput)
#     confirm_password = forms.CharField(
#         required=True,
#         max_length=23,
#         label='Confirm password',
#         widget=forms.PasswordInput)
#
#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super().__init__()
#
#     def clean_password_confirm(self):
#
#         new_password = self.cleaned_data['new_password']
#         confirm_password = self.cleaned_data['confirm_password']
#
#         if confirm_password != new_password:
#             raise forms.ValidationError("Password confirm doesn't match")
#
#         password_validation.validate_password(confirm_password, self.user)
#         password = confirm_password
#         return password
#
#     def save(self, commit=True):
#
#         password = self.cleaned_data['password']
#         self.user.set_password(password)
#         print("****" * 8)
#         print(password)
#         print("****" * 8)
#         if commit:
#             self.user.save(password=password)
#         return self.user



# class PasswordReset(PasswordResetForm):
#     email = forms.EmailField(
#         label=_("Email"),
#         max_length=254,
#         widget=forms.EmailInput(attrs={'autocomplete': 'email'})
#     )



