from django.urls import path, include
from . import views as users_view
from django.contrib.auth import views as auth_views

urlpatterns = [
	# path('index/', users_view.index, name='index'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('', users_view.signup_view, name='signup_view'),
	path('', 
		auth_views.LoginView.as_view(template_name='users/login.html'), 
		name='login'
	),
	path('password-reset/', 
		auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
		name='password_reset'
	),
	path('password-reset/done/', 
		auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
		name='password_reset_done'
	),
	path('password-reset/confirm/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
		name='password_reset_confirm'
	),
	path('logout/', 
		auth_views.LogoutView.as_view(template_name='users/logout.html'),
		name='logout'
	),
	path('profile/', users_view.profile_view, name='profile_view')
	# path('login/', views.login_view, name='login_view'),
	# path('success/', views.login_success, name='login_success')
]