from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User , Profile

@admin.register(User)
class UserAdmin(UserAdmin):
   add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2" ,"email", "first_name", "last_name", ),
            },
        ),
    )
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'date_active' ]
  list_per_page = 15 
  list_select_related = ['user']
  search_fields   = ['first_name__istartswith', 'last_name__istartswith']