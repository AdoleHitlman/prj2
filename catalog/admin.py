from django.contrib import admin

from catalog.models import Client, Category, Product,Blog,Version

#admin.site.register(Blog)
# Register your models here.
# admin.site.register(Client)
@admin.register(Blog)
class ClientBlog(admin.ModelAdmin):
    list_display = ('title',)
    # list_filter =
    search_fields = ('title',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')
    # list_filter =
    search_fields = ('name', 'message')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number')
    list_filter = ('product',)
    search_fields = ('product', 'version_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')

