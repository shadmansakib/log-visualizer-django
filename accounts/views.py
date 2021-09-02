from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import CustomPasswordChangeForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # todo: validate
        if not username or not password:
            print('Incorrect username or password')
            messages.error(request, 'Incorrect username or password')
            return render(request, 'accounts/login_form.html')

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, 'Incorrect username or password')
            return render(request, 'accounts/login_form.html')

        # login user
        login(request, user)
        return redirect('accounts:profile')

    return render(request, 'accounts/login_form.html')


@login_required(login_url='accounts:login')
def user_profile(request):
    form = CustomPasswordChangeForm(user=request.user, data=request.POST or None)

    if request.method == 'POST':
        if not form.is_valid():
            return render(request, 'accounts/user_profile.html', {'form': form})

        # save valid password, update session, redirect to same page with msg
        form.save()
        update_session_auth_hash(request, form.user)

        messages.success(request, 'Password changed')
        return redirect('accounts:profile')

    return render(request, 'accounts/user_profile.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('accounts:login')
