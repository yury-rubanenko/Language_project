from django.contrib import admin
from .models import Word, UserWord
# Register your models here.

class UserWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'user', 'is_learned')
    list_filter = ('learned_at',)

    def is_learned(self, obj):
        return obj.learned_at is not None
    
    is_learned.boolean = True
    is_learned.short_description = 'learned'


admin.site.register(Word)
admin.site.register(UserWord, UserWordAdmin)
