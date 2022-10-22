from django.contrib import admin
from .models import News,Category

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)