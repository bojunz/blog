from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30,min_length=2)
    password = forms.CharField(max_length=16,min_length=6,widget=forms.PasswordInput(attrs={
        'placeholder':'请输入密码',
    }))
    password_confirm = forms.CharField(max_length=16,min_length=6,
                                       widget=forms.PasswordInput(
                                           attrs={
                                               'placeholder':'请再次输入密码'
                                           }
                                       ))
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,min_length=2,widget=forms.TextInput(attrs={
        'placeholder':'请输入用户名',
    }))
    password = forms.CharField(max_length=16,min_length=6,widget=forms.PasswordInput(attrs={
        'placeholder':'请输入密码',
    }))