from django.contrib import admin

from .models import Comments, Posts


@admin.register(Posts)
class PostsModelAdmin(admin.ModelAdmin):
    list_display = ['short_description', 'full_description', 'is_draft', 'user', 'picture']
    search_fields = ['short_description', 'full_description', 'post_text']
    ordering = ['user']


@admin.register(Comments)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'text', 'is_published']
    search_fields = ['text', 'username']
    ordering = ['username']

    actions = ['publish_comments', 'make_draft']

    def publish_comments(self, request, queryset):
        queryset.update(is_published=Comments.LoanStatus.PUBLISHED)

    publish_comments.short_description = 'Mark selected as published'

    def make_draft(self, request, queryset):
        queryset.update(is_published=Comments.LoanStatus.IS_DRAFT)

    make_draft.short_description = 'Mark selected as draft'
