from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from .forms import ProfileForm1, ProfileForm2, UserForm, LoginForm, EditAccountForm, EditProfileForm1, EditProfileForm2, PasswordChangeForm
from django.http import Http404
from workout.models import Plan

# Create your views here.
def my_account_view(request):
    if request.user.is_active:      #login 됐는지 확인
        context = {
            'user': request.user,
        }
        return render(request, 'accounts/my_account.html', context)

    else:
        return redirect('accounts:login-register')


def login_register_view(request):
    if request.method == 'POST':
        if request.POST['action'] == 'register':
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                login(request, user)
                return redirect('accounts:register-profile')  # redirect to profile

        elif request.POST['action'] == 'login':
            login_form = LoginForm(data=request.POST)
            user_form = UserForm()
            if login_form.is_valid():
                # login the user
                user = login_form.get_user()
                login(request, user)
                return redirect('accounts:my-account')  # redirect to my_account

    else:
        user_form = UserForm()
        login_form = LoginForm()

    context = {
        'user_form': user_form,
        'login_form': login_form
    }
    return render(request, 'accounts/login_register.html', context)


def my_profile_view(request):
    if request.user.is_active:
        current_user = request.user
        if request.method == 'POST':
            if request.POST['action'] == 'edit_account': #account 정보 수정하기
                edit_account_form = EditAccountForm(request.POST, instance=request.user)
                edit_password_form = PasswordChangeForm(data=request.POST, user=request.user)
                edit_profile_form1 = EditProfileForm1(instance=request.user)
                edit_profile_form2 = EditProfileForm2(instance=request.user)
                if edit_account_form.is_valid() and edit_password_form.is_valid():
                    edit_account_form.save()
                    edit_password_form.save()
                    update_session_auth_hash(request, edit_password_form.user)
                    return redirect('accounts:my-profile')

            elif request.POST['action'] == 'edit_profile': #profile 정보 수정하기
                edit_profile_form1 = EditProfileForm1(request.POST, instance=request.user)
                edit_profile_form2 = EditProfileForm2(request.POST, instance=request.user)
                if edit_profile_form1.is_valid() and edit_profile_form2.is_valid():
                    # Essential code for storing profile data.
                    current_user.profile.height = edit_profile_form1.cleaned_data.get('height')
                    current_user.profile.weight = edit_profile_form1.cleaned_data.get('weight')
                    current_user.profile.gender = edit_profile_form1.cleaned_data.get('gender')
                    current_user.profile.birth_date = edit_profile_form1.cleaned_data.get('birth_date')
                    current_user.profile.frequency = edit_profile_form2.cleaned_data.get('frequency')
                    current_user.profile.aim = edit_profile_form2.cleaned_data.get('aim')
                    current_user.profile.goal = edit_profile_form2.cleaned_data.get('goal')
                    current_user.save()
                    return redirect('accounts:my-profile')
        else:  #for first page
            edit_account_form = EditAccountForm(instance=request.user)
            edit_password_form = PasswordChangeForm(user=request.user)
            edit_profile_form1 = EditProfileForm1(instance=request.user)
            edit_profile_form2 = EditProfileForm2(instance=request.user)

        context = {
            'edit_account_form': edit_account_form,
            'edit_password_form': edit_password_form,
            'edit_profile_form1': edit_profile_form1,
            'edit_profile_form2': edit_profile_form2,
            'user': request.user,
        }
        return render(request, 'accounts/my_profile.html', context)

    else:
        return redirect('accounts:my-account')


def logout_view(request): #using get method
    if request.user:
        if request.method == "POST":
            logout(request)
            return redirect('index')


def register_profile_view(request):
    current_user = request.user
    if request.method == 'POST':
        if request.POST['action'] == 'next':
            profile_form1 = ProfileForm1(request.POST)
            profile_form2 = ProfileForm2(request.POST)
            if profile_form1.is_valid():
                #current_user.refresh_from_db()  # load the profile instance created by the signal
                current_user.profile.height = profile_form1.cleaned_data.get('height') #Essential code for storing profile data.
                current_user.profile.weight = profile_form1.cleaned_data.get('weight')
                current_user.profile.gender = profile_form1.cleaned_data.get('gender')
                current_user.profile.birth_date = profile_form1.cleaned_data.get('birth_date')
                current_user.save() #Due to signal profile also be saved.
            else:
                raise Http404
        if request.POST['action'] == 'complete':
            profile_form1 = ProfileForm1(request.POST)
            profile_form2 = ProfileForm2(request.POST)
            if profile_form2.is_valid():
                # current_user.refresh_from_db()  # load the profile instance created by the signal
                current_user.profile.frequency = profile_form2.cleaned_data.get(
                    'frequency')  # Essential code for storing profile data.
                current_user.profile.aim = profile_form2.cleaned_data.get('aim')
                current_user.profile.goal = profile_form2.cleaned_data.get('goal')
                current_user.save()  # Due to signal profile also be saved.
                return redirect('index')
            else:
                raise Http404
    else:
        profile_form1 = ProfileForm1()
        profile_form2 = ProfileForm2()

    context = {
        'profile_form1': profile_form1,
        'profile_form2': profile_form2,
        'current_user': current_user,
    }

    return render(request, 'accounts/register_profile.html', context)
