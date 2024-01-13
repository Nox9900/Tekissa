
from django.shortcuts import render , redirect 
from django.urls import reverse_lazy 
from .forms import ArticleForm , UpdateArticleForm 
from .models import Article, Image
from django.views.generic import  UpdateView, DeleteView , View 

# Create your views here.

'''
  la vue qui s'occupe de la creation de l'article 
'''
class CreateArticle( View):
   template_name = 'shop/create_article.html'
   form_class = ArticleForm
   success_url = reverse_lazy('account:user_profile')

   def get(self, request, *args, **kwargs):
       self.user = request.user
       if not request.user.is_authenticated:
          return redirect('account:login')
       return render(request, self.template_name , context={'form': self.form_class})
     
  
   def post(self, request, *args, **kwargs):
     form = self.form_class(request.POST)
     if form.is_valid():
       article = form.save(commit=False)
       article.user = self.request.user 
       article.save() 
       images = self.request.FILES.getlist('images')
       for image in images: 
           Image.objects.create(article=article, thumbnail=image)         
       return redirect('account:user_profile')
     else: 
       pass       
       return render(request, self.template_name , context={'form': self.form_class})
       
       
class UpdateArticlesView(UpdateView):
    template_name: str = 'shop/update_article.html' 
    form_class = UpdateArticleForm
    model  = Article 
    context_object_name: str = 'article'
    success_url = reverse_lazy('account:user_profile')
    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['images'] = Image.objects.filter(article_id= self.kwargs['pk'])
      self.kwargs['images'] = context['images'] 
      return context 
     
    def form_valid(self, form):
      old_images = Image.objects.filter(article_id=self.kwargs['pk'])
      images = self.request.FILES.getlist('images')
       
      return super().form_valid(form)
    
class DeleteArticlesView(DeleteView):
  template_name = 'shop/delete_article.html'
  model = Article 
  context_object_name: str = 'article'
  success_url  = reverse_lazy('account:user_profile')


def voir_article(request, pk):
  
  object = Article.objects.get(pk=pk)
  img = Image.objects.all().filter(article=object)
  template = 'shop/voir_article.html'

  return render(request, template, context={
    'article': object,
    'img':img,
  })
