# Django Admin Site - Government Portal Style

Project Django mẫu theo phong cách cổng thông tin đơn vị nhà nước, có sẵn trang quản trị `/admin`.

## Tính năng
- Trang chủ kiểu cổng thông tin điện tử
- Banner/slideshow trang chủ
- Thông báo nổi bật
- Liên kết nhanh
- Tin tức có ảnh
- Tài liệu PDF
- Trang cơ cấu tổ chức
- Chân trang có khu vực bản đồ liên hệ
- Quản trị nội dung trực tiếp tại `/admin`

## Cách chạy
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Truy cập
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Thứ tự nhập liệu nên làm
1. Thông tin đơn vị
2. Liên kết nhanh
3. Thông báo nổi bật
4. Banner trang chủ
5. Tin tức
6. Danh mục tài liệu và Tài liệu PDF
7. Cơ cấu tổ chức

## Gợi ý bản đồ liên hệ
Trong Admin → Thông tin đơn vị → `map_embed_url`, dán link Google Maps Embed.
Ví dụ dạng:
`https://www.google.com/maps/embed?...`
