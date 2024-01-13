
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin




from shop.data import ArticleInTemplate
from shop.models import Article, Image
from .models import Profile
from .forms import LoginForm, RegisterForm, ProfileForm, UserForm
from . import url_name as Path_Url

# Create your views here.


"""
 Get the current user model on this project 
 permet d'utiliser le model utilisateur pour ce project 

"""
User = get_user_model()

"""
 register_user is the view which handles the user's registration
 la vue register_user s'occupe de la creation des utilisateus sur le 
 project 

"""


def register_user(request, *args, **kwargs):  # fbv (function base view , vue fondé sur les fonctions)
    form = RegisterForm

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
        
            user = User.objects.create_user(username=username, password=password, email=email)

            if user is not None:
                user_profile = Profile()
                user_profile.user = user
                return redirect(Path_Url.LOGIN_URL_BY_APP_NAME)
    else: pass

    return render(request, 'account/register.html', context={'form': form})


""""
  LoginUser is a cbv (class base view ) which is responsible of the login process
  La classe LoginUser est responsable de connexion de l'utilisateur 

"""

class LoginUser(View):
    template_name = 'account/login.html'
    login_form = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # empêche l'access a la vue de connexion si l'utilisateur est déja connecté
            return redirect(Path_Url.USER_PROFIL_URL_BY_APP_NAME)
        return render(request, self.template_name, context={'login_form': self.login_form})

    def post(self, request, *args, **kwargs):
        form = self.login_form(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(Path_Url.USER_PROFIL_URL_BY_APP_NAME)
            else:
                # renvoie un message d'erreur si les informations saisie ne sont pas valident
                messages.error(request, "Le nom d'utilisateur  ou le mot de passe est incorrect")
                return render(request, self.template_name, context={'login_form': form})
        else:
            return render(request, self.template_name, context={'login_form': form})


"""
  la vue qui s'occupe de deconnecté l'utilisateur  
"""


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect(Path_Url.LOGIN_URL_BY_APP_NAME)
    logout(request)
    return redirect(Path_Url.LOGIN_URL_BY_APP_NAME)


class UserProfile(LoginRequiredMixin, View):
    login_url: str = Path_Url.LOGIN_URL_BY_APP_NAME
    template_name: str = 'account/profil.html'
    

    def get(self, request, *args, **kwargs):
        articles = []
        if not request.user.is_authenticated:
            return redirect(Path_Url.LOGIN_URL_BY_APP_NAME)
        articles_queryset = Article.objects.filter(user=request.user)
        for article in articles_queryset:
            image_firt = Image.objects.filter(article_id=article.id).first()
            image_article_count = Image.objects.filter(
                article_id=article.id).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

        return render(request, self.template_name, context={ 'articles': articles })


'''
 mettre a jour le profil de l'utilisateur 
'''


class UserUpdateProfile(LoginRequiredMixin, View,):
    login_url: str = Path_Url.LOGIN_URL_BY_APP_NAME
    templates_name: str = 'account/user_update_profile.html'

    def get(self, request, *args, **kwargs):
        profil = get_object_or_404(Profile, pk=kwargs.get('pk'))
        user = User.objects.get(pk=profil.user_id)
        profil_form = ProfileForm(instance=profil)
        user_form = UserForm(instance=user)

        if self.request.user.profile.pk != self.kwargs['pk']:
            return redirect(Path_Url.USER_PROFIL_URL_BY_APP_NAME)
        return render(request, self.templates_name, {'form': profil_form, 'form2': user_form} )
    
    def  post(self, request, *args, **kwargs): 
        profil = get_object_or_404(Profile, pk=kwargs.get('pk'))
        user = User.objects.get(pk=profil.user_id)
        profil_form = ProfileForm(request.POST, request.FILES, instance=profil)
        user_form = UserForm(request.POST, instance = user)
        if user_form.is_valid() and profil_form.is_valid():
           user.save()
           profil.save()
           messages.success(request, 'Modification appliquer avec success')
           
           return redirect("account:update_profile", **kwargs)
        #  return render(request, self.templates_name, {'form': user_form, 'form2': profil_form})    
        else: 
          messages.error(request, "Formulaire invalid")
          return redirect("account:update_profile", **kwargs)
          
        #return render(request, self.templates_name, {'form': user_form, 'form2': profil_form})


class ResetPasswordView (SuccessMessageMixin, PasswordResetView):
    template_name = 'account/passwdReset.html'
    email_template_name = 'account/passwd_reset_email.txt'
    subject_template_name = 'account/passwd_reset_subject.txt'
    success_message =  "Nous vous avons envoyé des instructions sur votre adresse mail. Merci de vérifier ce dernier."
    success_url = reverse_lazy('account:login')
    
    