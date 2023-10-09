from django.contrib import admin
from catalog.models import Category, Discount, Product, Promocode, Seller, Order, Cashback


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'articul', 'category', 'seller')
    search_fields = ('name', 'articul', 'seller__name', 'seller__country', 'category__name')
    list_select_related = ('category', 'seller')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'date_start', 'date_end')
    search_fields = ('name', 'percent')


class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'date_start', 'date_end', 'is_cumulative')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Promocode, PromocodeAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Cashback)
