from django.contrib import admin

from places.models import (
    Place, Category, Review, Media
)


class MediaInline(admin.TabularInline):
    model = Media
    extra = 0


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    list_filter = ('has_wifi', 'name',)
    list_display = ('name', 'user', 'category', 'has_wifi',
                    'review_count', 'is_active')
    list_editable = ('category', 'has_wifi', 'is_active')
    actions = ('set_wifi_true',)
    search_fields = ('name', 'user__username')
    view_on_site = True
    inlines = [
        MediaInline,
        ReviewInline,
    ]

    def set_wifi_true(self, request, queryset):
        queryset.update(has_wifi=True)

    set_wifi_true.short_description = 'Mahmut'


admin.site.register(Place, PlaceAdmin)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Media)
