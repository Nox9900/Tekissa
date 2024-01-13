from django.urls import path
from .views import LoginUser, register_user, UserProfile, logout_user, UserUpdateProfile, ResetPasswordView
from django.contrib.auth import views

from . import url_name as  Path_Url

app_name = 'account'  # est un espace de nom qui permet d'encasptuler les views par rapport au nom de leur application a partir de leur nom d'url


urlpatterns = [

    path('enregistrer/', register_user, name=Path_Url.REGISTER_VIEW_NAME),
    path('connexion/', LoginUser.as_view(), name=Path_Url.LOGIN_VIEW_NAME),
    path('deconnexion/', logout_user, name=Path_Url.LOGOUT_VIEW_NAME),
    path('profil/', UserProfile.as_view(), name=Path_Url.USER_PROFIL_VIEW_NAME),
    path('update_profile/<int:pk>/', UserUpdateProfile.as_view(), name=Path_Url.UPDATE_PROFIL_VIEW_NAME),
    path('reinitialisation_du_mot_de_passe/', ResetPasswordView.as_view(), name='password_reset'),
    # path('message_de_reinitialisation/', views.PasswordResetDoneView.as_view(template_name='account/passwd_reset_done.html'), name='password_reset_done'),
    path('reinitialisation/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='account/passwd_reset_confirm.html'), name='password_reset_confirm'),
    path('reinitialisation_complete/', views.PasswordResetCompleteView.as_view(template_name='account/passwd_reset_complete.html'), name='password_reset_complete'),
]
