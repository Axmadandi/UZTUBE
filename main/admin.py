from django.contrib import admin
from .models import*
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ['title', 'category','id']
	list_display_links = ['title', ]
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = Movie