from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .models import Clothes, ClothesSet, ClothesSetReview
from .models import CategoryData

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('user_id', 'gender', 'birthday', 'is_staff', 'is_active',)
    list_filter = ('gender', 'birthday', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('user_id', 'password', 'birthday', 'gender')}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'password1', 'password2', 'birthday', 'gender','is_staff', 'is_active')
        }),
    )
    search_fields = ('user_id',)
    ordering = ('user_id',)
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Clothes)
admin.site.register(ClothesSet)
admin.site.register(ClothesSetReview)
admin.site.register(CategoryData)

