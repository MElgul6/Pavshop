from django.contrib import admin

from .models import Billing_details, Shipping_info,CartItem,Cart

admin.site.register(CartItem)
admin.site.register(Cart)


@admin.register(Billing_details)
class BillingAdmin(admin.ModelAdmin):
    search_fields = ('firstname',)
    list_filter = ('city',)
    list_display=('firstname','lastname')
   
@admin.register(Shipping_info)
class ShippingAdmin(admin.ModelAdmin):
    search_fields = ('first_name',)
    list_filter = ('city',)
    list_display=('first_name','last_name')