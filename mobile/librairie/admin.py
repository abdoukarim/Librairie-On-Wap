# -*- coding: utf-8 -*-
"""
Administration interface options of ``blog`` application.
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mobile.librairie.models import Author, Publisher, Theme, Category, Livre

class AuthorAdmin(admin.ModelAdmin):
    """
    Administration interface options of ``Author`` model.
    """
    list_display = ('name', 'contact','status',)
    search_fields = ('name',)
    #date_hierarchy = 'publication_date'
    fieldsets = (
        (_('Description'), {'fields': ('name', 'contact','description','status',)}),
    )
    save_on_top = True
    radio_fields = {'status': admin.VERTICAL}
    #prepopulated_fields = {'slug': ('title',)}

class PublisherAdmin(admin.ModelAdmin):
	"""
	Administration interface options of ``Publisher`` model.
	"""
	list_display = ('name',)

class ThemeInline(admin.TabularInline):
     model = Theme
     extra = 0
    
class CategoryAdmin(admin.ModelAdmin):
	"""
	Administration interface options of ``Category`` model.
	"""
	list_display = ('name',)
	inlines = [ThemeInline]
    
class ThemeAdmin(admin.ModelAdmin):
	"""
	Administration interface options of ``Theme`` model.
	"""
	list_display = ('slug', 'monthTheme', 'toggle_monthTheme', 'category')
	#radio_fields = {'monthTheme': admin.VERTICAL}
    
    
class LivreAdmin(admin.ModelAdmin):
    """
    Administration interface options of ``Livre`` model.
    """
    list_display = ('title', 'publisher', 'theme')
    search_fields = ('title',)
    fieldsets = (
		('Liens', {
            'classes': ('collapse',),
            'fields': ('authors', 'theme', 'publisher')}),
		
        (_('Information'), {
			'classes': ('collapse',),
			'fields': ('title','price', 'pages', 'height', 'width', 'isbn', 'language')}),
		
		(_('Resume'), {
			'classes':('collapse',),
			'fields': ('resume',)}),
    )
    #date_hierarchy = 'creation_date'
    save_on_top = True
    #prepopulated_fields = {'slug': ('name',)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Livre, LivreAdmin)
