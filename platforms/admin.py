from django.contrib import admin
from .models import Word, UserWord
# Register your models here.

class LearnedFilter(admin.SimpleListFilter):
    title = 'Learned Status'
    parameter_name = 'is_learned'

    def lookups(self, request, model_admin):
        return(
        ('learned', 'Learned'),
        ('not_learned', 'Not Learned'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'learned':
            return queryset.filter(learned_at__isnull=False)
        if self.value() == 'not_learned':
            return queryset.filter(learned_at__isnull=True)

class UserWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'user')
    list_filter = (LearnedFilter,)



admin.site.register(Word)
admin.site.register(UserWord, UserWordAdmin)

