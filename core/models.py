from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    ministry_name = models.CharField(max_length=255, default="Bộ Nông nghiệp và Môi trường")
    parent_unit = models.CharField(max_length=255, default="Trung tâm Quy hoạch và Điều tra tài nguyên nước quốc gia")
    unit_name = models.CharField(max_length=255, default="Trung tâm Cảnh báo và Dự báo tài nguyên nước")
    short_name = models.CharField(max_length=120, default="CB&DB TNN")
    portal_name = models.CharField(max_length=255, default="Cổng thông tin điện tử")
    hero_title = models.CharField(max_length=255, default="Cổng thông tin điện tử Trung tâm Cảnh báo và Dự báo tài nguyên nước")
    hero_subtitle = models.TextField(default="Cập nhật thông tin chỉ đạo điều hành, tin tức chuyên ngành, tài liệu công bố, chương trình công tác và đầu mối liên hệ phục vụ hoạt động cảnh báo, dự báo tài nguyên nước.")
    address = models.CharField(max_length=255, blank=True)
    hotline = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    intro = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    footer_note = models.CharField(max_length=255, blank=True, help_text="Ví dụ: Cơ quan chủ quản, ghi chú chân trang...")
    map_embed_url = models.URLField(blank=True, help_text="Dán link Google Maps Embed để hiển thị bản đồ ở chân trang")

    class Meta:
        verbose_name = "Thông tin đơn vị"
        verbose_name_plural = "Thông tin đơn vị"

    def __str__(self):
        return self.unit_name


class BannerSlide(TimeStampedModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="banners/")
    button_text = models.CharField(max_length=50, blank=True, default="Xem thêm")
    button_link = models.CharField(max_length=255, blank=True, help_text="Ví dụ: /tin-tuc/ hoặc https://...")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "-id"]
        verbose_name = "Banner trang chủ"
        verbose_name_plural = "Banner trang chủ"

    def __str__(self):
        return self.title


class Notice(TimeStampedModel):
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    link = models.CharField(max_length=255, blank=True, help_text="Ví dụ: /tai-lieu/ hoặc link ngoài")
    published_at = models.DateField()
    is_pinned = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-is_pinned", "-published_at", "-id"]
        verbose_name = "Thông báo nổi bật"
        verbose_name_plural = "Thông báo nổi bật"

    def __str__(self):
        return self.title


class QuickLink(TimeStampedModel):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Liên kết nhanh"
        verbose_name_plural = "Liên kết nhanh"

    def __str__(self):
        return self.title


class NewsPost(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    published_at = models.DateField()
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at", "-id"]
        verbose_name = "Tin tức"
        verbose_name_plural = "Tin tức"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})


class DocumentCategory(TimeStampedModel):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Danh mục tài liệu"
        verbose_name_plural = "Danh mục tài liệu"

    def __str__(self):
        return self.name


class Document(TimeStampedModel):
    category = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="documents/")
    published_at = models.DateField()
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at", "title"]
        verbose_name = "Tài liệu PDF"
        verbose_name_plural = "Tài liệu PDF"

    def __str__(self):
        return self.title


class OrganizationUnit(TimeStampedModel):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=120, blank=True)
    unit_type = models.CharField(max_length=120, default="Phòng chuyên môn")
    scope = models.CharField(max_length=255, blank=True, help_text="Ví dụ: Miền Bắc, toàn quốc...")
    duties_summary = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Phòng/Bộ phận"
        verbose_name_plural = "Phòng/Bộ phận"

    def __str__(self):
        return self.name


class LeadershipMember(TimeStampedModel):
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    department = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="leaders/", blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "full_name"]
        verbose_name = "Lãnh đạo/nhân sự"
        verbose_name_plural = "Lãnh đạo/nhân sự"

    def __str__(self):
        return f"{self.full_name} - {self.position}"


class LeadershipAssignment(TimeStampedModel):
    title = models.CharField(max_length=200)
    lead = models.ForeignKey(LeadershipMember, on_delete=models.SET_NULL, null=True, blank=True, related_name="assignments")
    supporting_text = models.CharField(max_length=255, blank=True, help_text="Ví dụ: Phối hợp cùng các Phó Giám đốc hoặc các phòng liên quan")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Mảng lãnh đạo phụ trách"
        verbose_name_plural = "Mảng lãnh đạo phụ trách"

    def __str__(self):
        return self.title


class BulletinIssue(TimeStampedModel):
    TYPE_MONTH = "month"
    TYPE_SEASON = "season"
    TYPE_YEAR = "year"
    TYPE_SPECIAL = "special"
    BULLETIN_TYPE_CHOICES = [
        (TYPE_MONTH, "Bản tin tháng"),
        (TYPE_SEASON, "Bản tin mùa"),
        (TYPE_YEAR, "Bản tin năm"),
        (TYPE_SPECIAL, "Chuyên đề"),
    ]

    title = models.CharField(max_length=255)
    bulletin_type = models.CharField(max_length=20, choices=BULLETIN_TYPE_CHOICES, default=TYPE_MONTH)
    slug = models.SlugField(max_length=255, unique=True)
    period_label = models.CharField(max_length=120, blank=True, help_text="Ví dụ: Tháng 3/2026, Mùa khô 2026, Năm 2025...")
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="bulletins/", blank=True, null=True)
    file = models.FileField(upload_to="bulletins/files/", blank=True, null=True)
    published_at = models.DateField()
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-published_at", "title"]
        verbose_name = "Bản tin"
        verbose_name_plural = "Bản tin"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bulletin_detail", kwargs={"slug": self.slug})
