from django.contrib import admin
from .models import Subscription, Cards

# Register your models here.

class SubscriptionAdmin(admin.ModelAdmin):
    

    readonly_fields = ('sub_number', 'date', 'user')


    fields = ('sub_number', 'user', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'date', 'price')


    list_display = ('full_name', 'user', 'email',
                    'sub_number', 'date', 'price')
    

    ordering = ('-date',)


class CardsAdmin(admin.ModelAdmin):
    fields = ('duration', 'price', 'saving', 'offering',)


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Cards, CardsAdmin)