from django.shortcuts import render, redirect
from . forms import UserRegisterForm, ProfileUpdateForm, ProfilePictureUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.


# def index(request):
# 	return render(request, 'users/index.html')

def signup_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'users/index.html', {'signup_form': form})


def profile_view(request):
	pass
	# if request.method == 'POST':
 #        profile_picture_update = (request.POST, request.FILES, instance=request.user.profile)
 #        profile_update = ProfileUpdateForm(request.POST, instance=request.user)

 #        if profile_update.is_valid() and profile_picture_update.is_valid():
 #            profile_update.save()
 #            profile_picture_update.save()
 #            messages.success(request, f'Account has been updated.')
 #            return redirect('profile')
 #    else:
 #        profile_update = ProfileUpdateForm(instance=request.user)
 #        profile_picture_update = ProfilePictureUpdateForm(instance=request.user.profile)

 #    return render(request, 'users/profile.html', {'profile_update': profile_update, 'profile_picture_update': profile_picture_update})