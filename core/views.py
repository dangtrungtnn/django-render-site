from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import (
    SiteSettings, BannerSlide, Notice, QuickLink, NewsPost, Document, OrganizationUnit,
    LeadershipMember, LeadershipAssignment, BulletinIssue,
)


def get_site_settings():
    return SiteSettings.objects.order_by("id").first()


def global_context():
    return {
        "site_settings": get_site_settings(),
        "header_notices": Notice.objects.filter(is_published=True)[:5],
        "quick_links": QuickLink.objects.filter(is_active=True)[:8],
    }


def _leadership_structure():
    members = list(LeadershipMember.objects.filter(is_active=True))
    director = next((m for m in members if m.position.strip().lower() == "giám đốc"), None)
    deputies = [m for m in members if "phó giám đốc" in m.position.lower()]
    others = [m for m in members if m not in ([director] if director else []) + deputies]
    return director, deputies, others


def home(request):
    context = global_context()
    director, deputies, others = _leadership_structure()
    context.update(
        {
            "slides": BannerSlide.objects.filter(is_active=True)[:5],
            "featured_news": NewsPost.objects.filter(is_published=True, is_featured=True)[:4],
            "latest_news": NewsPost.objects.filter(is_published=True)[:8],
            "latest_documents": Document.objects.filter(is_published=True)[:8],
            "featured_documents": Document.objects.filter(is_published=True, is_featured=True)[:5],
            "leaders": LeadershipMember.objects.filter(is_active=True)[:6],
            "org_units": OrganizationUnit.objects.filter(is_active=True)[:5],
            "featured_notices": Notice.objects.filter(is_published=True)[:6],
            "leadership_assignments": LeadershipAssignment.objects.filter(is_active=True)[:6],
            "featured_bulletins": BulletinIssue.objects.filter(is_published=True, is_featured=True)[:4],
            "latest_bulletins": BulletinIssue.objects.filter(is_published=True)[:8],
            "director": director,
            "deputies": deputies,
            "other_members": others,
        }
    )
    return render(request, "core/home.html", context)


def about(request):
    context = global_context()
    context["org_units"] = OrganizationUnit.objects.filter(is_active=True)
    return render(request, "core/about.html", context)


def contact(request):
    context = global_context()
    return render(request, "core/contact.html", context)


def structure(request):
    context = global_context()
    director, deputies, others = _leadership_structure()
    context.update(
        {
            "members": LeadershipMember.objects.filter(is_active=True),
            "org_units": OrganizationUnit.objects.filter(is_active=True),
            "director": director,
            "deputies": deputies,
            "other_members": others,
            "assignments": LeadershipAssignment.objects.filter(is_active=True),
        }
    )
    return render(request, "core/structure.html", context)


def news_list(request):
    query = request.GET.get("q", "").strip()
    items = NewsPost.objects.filter(is_published=True)
    if query:
        items = items.filter(Q(title__icontains=query) | Q(summary__icontains=query) | Q(content__icontains=query))
    context = global_context()
    context.update({"news_items": items, "query": query})
    return render(request, "core/news_list.html", context)


def news_detail(request, slug):
    item = get_object_or_404(NewsPost, slug=slug, is_published=True)
    related = NewsPost.objects.filter(is_published=True).exclude(id=item.id)[:4]
    context = global_context()
    context.update({"item": item, "related": related})
    return render(request, "core/news_detail.html", context)


def document_list(request):
    query = request.GET.get("q", "").strip()
    docs = Document.objects.filter(is_published=True)
    if query:
        docs = docs.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query))
    context = global_context()
    context.update({"documents": docs, "query": query})
    return render(request, "core/document_list.html", context)


def bulletin_list(request):
    query = request.GET.get("q", "").strip()
    bulletin_type = request.GET.get("type", "").strip()
    items = BulletinIssue.objects.filter(is_published=True)
    if query:
        items = items.filter(Q(title__icontains=query) | Q(summary__icontains=query) | Q(content__icontains=query) | Q(period_label__icontains=query))
    if bulletin_type:
        items = items.filter(bulletin_type=bulletin_type)
    context = global_context()
    context.update(
        {
            "bulletins": items,
            "query": query,
            "selected_type": bulletin_type,
            "type_choices": BulletinIssue.BULLETIN_TYPE_CHOICES,
        }
    )
    return render(request, "core/bulletin_list.html", context)


def bulletin_detail(request, slug):
    item = get_object_or_404(BulletinIssue, slug=slug, is_published=True)
    related = BulletinIssue.objects.filter(is_published=True).exclude(id=item.id)[:4]
    context = global_context()
    context.update({"item": item, "related": related})
    return render(request, "core/bulletin_detail.html", context)
