from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from tripapp.models import YourStory, ContactUs, YourTrip

User = get_user_model()


class ProfileForm(forms.ModelForm):  #########register
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    number = forms.CharField(max_length=255)
    email = forms.EmailField(required=True, )
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'number', 'email', 'username', 'password', 'password2']

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):  ####################login
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class AddYourStory(forms.ModelForm):  ##########addstory
    title = forms.CharField()
    story = forms.CharField()
    author = forms.CharField(max_length=255)
    image = forms.ImageField()
    date = forms.CharField()
    caption = forms.CharField()

    class Meta:
        model = YourStory
        fields = ["title", "story", "author", "image", "date", "caption"]


class AddYourTrip(forms.ModelForm):  ##########addstory
    title = forms.CharField()
    tagline = forms.CharField()
    story = forms.CharField()
    image = forms.ImageField()

    class Meta:
        model = YourTrip
        fields = ["title", "tagline", "story", "image"]


class ContactForm(forms.ModelForm):####################contact
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    msg = forms.CharField()

    class Meta:
        model = ContactUs
        fields = ["first_name", "last_name", "email", "msg"]



