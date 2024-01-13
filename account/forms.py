
from django import forms
from account.models import Profile, User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': "Nom d'utilisateur"

        }
    ))
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-input ',
        'type': 'email',
        'placeholder': 'E-mail'

    }))

    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'type': 'password',
        'placeholder': 'Mot de passe'

    }))



class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': "Nom d'utilisateur",

        }
    ))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': "Mot de passe",
        'type': 'password',

    }))


class ProfileForm (forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['sex'].widget.attrs = {
            'class': "form-input", "placeholder": "Nom d'utilisateur"}
        self.fields['address'].widget.attrs = {
            "class": "form-input", "placeholder": "Address"}
        self.fields['cellphone'].widget.attrs = {
            "class": "form-input", "placeholder": "Numero de telephone"}
        self.fields['picture'].widget.attrs = {
            "class": "form-input", "placeholder": "Votre photo"}

    class Meta:
        model = Profile
        exclude = ['user']
        widget = {
            "sex": forms.Select(),
            "address": forms.TextInput(),
            "cellphone": forms.NumberInput(),
            "picture": forms.FileField(),
        }


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': "form-input", "placeholder": "Nom d'utilisateur"}
        self.fields['first_name'].widget.attrs = {
            "class": "form-input", "placeholder": "Prenoms"}
        self.fields['last_name'].widget.attrs = {
            "class": "form-input", "placeholder": "Noms"}
        self.fields['email'].widget.attrs = {
            "class": "form-input", "placeholder": "Email"}

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widget = {
            "username": forms.TextInput(attrs={"class": "form-input", "placeholder": "Nom d'utilisateur"}),
            "first_name": forms.TextInput(),
            "last_name": forms.TextInput(),
            "email": forms.EmailInput()
        }

