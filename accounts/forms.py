from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


class UserForm(UserCreationForm):
    username = forms.CharField(label='아이디', label_suffix='')
    first_name = forms.CharField(max_length=30, required=False, label='이름', label_suffix='')
    email = forms.EmailField(max_length=30, label='이메일', label_suffix='')
    password1 = forms.CharField(label='비밀번호', label_suffix='', widget=forms.PasswordInput())
    password2 = forms.CharField(label='비밀번호 재입력', label_suffix='', widget=forms.PasswordInput())

    username.widget.attrs.update({'autocomplete': 'off'})
    first_name.widget.attrs.update({'autocomplete': 'off'})
    email.widget.attrs.update({'autocomplete': 'off'})
    password1.widget.attrs.update({'autocomplete': 'off'})
    password2.widget.attrs.update({'autocomplete': 'off'})

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2',
        ]


class EditAccountForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditAccountForm, self).__init__(*args, **kwargs)
        try:
            self.fields['username'].initial = self.instance.username
            self.fields['first_name'].initial = self.instance.first_name
            self.fields['email'].initial = self.instance.email
        except User.DoesNotExist:
            pass

    username = forms.CharField(label='아이디', label_suffix='')
    first_name = forms.CharField(max_length=30, required=False, label='이름', label_suffix='')
    email = forms.EmailField(max_length=30, label='이메일', label_suffix='')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='아이디', label_suffix='')
    password = forms.CharField(label='비밀번호', label_suffix='', widget=forms.PasswordInput())


class ProfileForm1(ModelForm):
    GENDER_CHOICES = (
        ('male', '남성'),
        ('female', '여성')
    )
    ADDRESS_CHOICES = (
        ('seoul', '서울특별시'),
        ('busan', '부산광역시'),
        ('daegu', '대구광역시'),
        ('daejeon', '대전광역시'),
        ('incheon', '인천광역시'),
        ('gwangju', '광주광역시'),
        ('ulsan', '울산광역시'),
        ('gyeonggi', '경기도'),
        ('gangwon', '강원도'),
        ('chungcheongbuk', '충청북도'),
        ('chungcheongnam', '충청남도'),
        ('jeollabuk', '전라북도'),
        ('jeollanam', '전라남도'),
        ('gyeongsangbuk', '경상북도'),
        ('gyeongsangnam', '경상남도'),
        ('jeju', '제주특별자치도'),
        ('sejong', '세종특별자치시'),
    )

    address = forms.CharField(label='사는 곳', label_suffix='', widget=forms.Select(choices=ADDRESS_CHOICES))
    birth_date = forms.DateField(label='생년월일', label_suffix='', widget=forms.DateInput(),
                                 help_text='Requried format 19xx-xx-xx')
    gender = forms.CharField(label='성별', label_suffix='', widget=forms.Select(choices=GENDER_CHOICES))
    height = forms.FloatField(label='신장', label_suffix='')
    weight = forms.FloatField(label='몸무게', label_suffix='')

    class Meta:
        model = Profile
        fields = [
            'gender',
            'address',
            'birth_date',
            'height',
            'weight',
        ]


class ProfileForm2(ModelForm):
    FREQUENCY = (
        ('daliy', '매일'),
        ('usually', '주 5회이상'),
        ('often', '주 3회이상'),
        ('rarely', '주 1회이상'),
        ('never', '안해요..')
    )
    AIM = (
        ('diet', '다이어트'),
        ('bulkup', '벌크업'),
        ('wellbing', '건강유지'),
        ('fashion', '패션헬스'),
    )

    frequency = forms.CharField(label='운동 빈도', label_suffix='', help_text='본인의 운동빈도를 설정해주세요.', widget=forms.Select(choices=FREQUENCY))
    aim = forms.CharField(label='운동 목적', label_suffix='', help_text='본인의 운동목적을 설정해주세요.', widget=forms.Select(choices=AIM))
    goal = forms.FloatField(label='운동 목표', label_suffix='',)

    class Meta:
        model = Profile
        fields = [
            'frequency',
            'aim',
            'goal',
        ]


class EditProfileForm1(ProfileForm1):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm1, self).__init__(*args, **kwargs)
        try:
            self.fields['height'].initial = self.instance.profile.height
            self.fields['weight'].initial = self.instance.profile.weight
            self.fields['birth_date'].initial = self.instance.profile.birth_date
            self.fields['gender'].initial = self.instance.profile.gender
        except User.DoesNotExist:
            pass


class EditProfileForm2(ProfileForm2):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm2, self).__init__(*args, **kwargs)
        try:
            self.fields['frequency'].initial = self.instance.profile.frequency
            self.fields['aim'].initial = self.instance.profile.aim
            self.fields['goal'].initial = self.instance.profile.goal
        except User.DoesNotExist:
            pass


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='현재 비밀번호', label_suffix='', widget=forms.PasswordInput(), required=False)
    new_password1 = forms.CharField(label='새로운 비밀번호', label_suffix='', widget=forms.PasswordInput(), required=False)
    new_password2 = forms.CharField(label='새로운 비밀번호 확인', label_suffix='', widget=forms.PasswordInput(), required=False)
