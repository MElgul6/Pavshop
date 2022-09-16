from django.contrib import admin


from .models import Contact,Subscriber, Team

admin.site.register(Subscriber)
admin.site.register(Team)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('subject',)
    list_filter = ('fullname',)
    list_display=('fullname','created_at')
