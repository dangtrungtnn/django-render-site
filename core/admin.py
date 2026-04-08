from django.contrib import admin
from .models import (
    SiteSettings, BannerSlide, Notice, QuickLink, NewsPost, DocumentCategory, Document,
    OrganizationUnit, LeadershipMember, LeadershipAssignment, BulletinIssue,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("unit_name", "parent_unit", "email", "hotline", "updated_at")


@admin.register(BannerSlide)
class BannerSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("title", "subtitle")


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "is_pinned", "is_published")
    list_filter = ("is_pinned", "is_published", "published_at")
    search_fields = ("title", "summary")


@admin.register(QuickLink)
class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "link")


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "is_published", "is_featured")
    list_filter = ("is_published", "is_featured", "published_at")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    search_fields = ("name",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at", "is_published", "is_featured")
    list_filter = ("category", "is_published", "is_featured", "published_at")
    search_fields = ("title", "description")


@admin.register(OrganizationUnit)
class OrganizationUnitAdmin(admin.ModelAdmin):
    list_display = ("name", "unit_type", "scope", "order", "is_active")
    list_filter = ("unit_type", "is_active")
    search_fields = ("name", "short_name", "scope", "duties_summary")


@admin.register(LeadershipMember)
class LeadershipMemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "department", "order", "is_active")
    list_filter = ("is_active", "department")
    search_fields = ("full_name", "position", "department")


@admin.register(LeadershipAssignment)
class LeadershipAssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "lead", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description", "supporting_text", "lead__full_name")


@admin.register(BulletinIssue)
class BulletinIssueAdmin(admin.ModelAdmin):
    list_display = ("title", "bulletin_type", "period_label", "published_at", "is_published", "is_featured")
    list_filter = ("bulletin_type", "is_published", "is_featured", "published_at")
    search_fields = ("title", "summary", "content", "period_label")
    prepopulated_fields = {"slug": ("title",)}
