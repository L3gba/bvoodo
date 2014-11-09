from django.contrib import admin
from voodoo.models import Category, SubCategory, NewsItem, Site

class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name', 'category_slug']
    

class SubCategoryAdmin(admin.ModelAdmin):
    fields = ['category', 'sport_name', 'sport_description']

    
class SiteAdmin(admin.ModelAdmin):
    fields = ['category', 'name', 'url', 'promo_image', 'rating']
    
    
class NewsItemAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'body', 'site', 'sport_name', 'url', 'image']
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(NewsItem, NewsItemAdmin)