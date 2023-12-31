from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id","user","title","description","price","created_date","updated_date","negotiable","image_display"]
    list_filter = ["negotiable","created_at","updated_at"]
    actions = ["make_auction_as_false","make_auction_as_true"]
    fieldsets = (
        ("Общее",{
            "fields":("title","description","user","image"),
            "classes":["collapse"]
        }),
        ("Финансы",{
            "fields":("price","negotiable"),
            "classes": ["collapse"]
        })
    )



    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(negotiable=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(negotiable=True)



admin.site.register(Advertisements,AdvertisementAdmin)


#До встречи!Удачи,успехов и всего наилучшего!!!
