from django.contrib import admin
from .models import Category, Person, Event, Comment ,HistoricalPeriod


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name',)  

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography_short')
    search_fields = ('name',)
    list_filter = ('categories',)  

    def biography_short(self, obj):
        return obj.biography[:60] + '...' if len(obj.biography) > 60 else obj.biography
    biography_short.short_description = 'Biography'

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description_short')
    list_filter = ('date', 'categories')
    search_fields = ('title',)

    def description_short(self, obj):
        return obj.description[:75] + '...' if len(obj.description) > 75 else obj.description
    description_short.short_description = 'Description'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_short', 'user', 'event', 'created_at')
    list_filter = ('created_at', 'user', 'event')
    search_fields = ('content', 'user__username', 'event__title')

    def content_short(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_short.short_description = 'Content'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(HistoricalPeriod)