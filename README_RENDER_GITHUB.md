# Hướng dẫn đẩy project lên GitHub và deploy lên Render

## 1) Chuẩn bị local
Trong thư mục project:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Nếu chạy local bình thường thì chuyển sang bước GitHub.

## 2) Tạo repository trên GitHub bằng giao diện web
1. Đăng nhập GitHub.
2. Bấm **New repository**.
3. Đặt tên repo, ví dụ: `tccbdb-portal`.
4. Chọn **Public** hoặc **Private**.
5. Bấm **Create repository**.

## 3) Đẩy code từ máy lên GitHub
Mở terminal trong thư mục project và chạy:

```bash
git init
git add .
git commit -m "Initial commit for Render deploy"
git branch -M main
git remote add origin https://github.com/TEN_TAI_KHOAN_GITHUB/TEN_REPO.git
git push -u origin main
```

Nếu Git yêu cầu đăng nhập, đăng nhập bằng trình duyệt hoặc dùng GitHub token.

## 4) Tạo web service trên Render
1. Đăng nhập Render.
2. Chọn **New +** → **Web Service**.
3. Kết nối tài khoản GitHub.
4. Chọn đúng repository vừa push.
5. Điền:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn config.wsgi:application`
6. Chọn instance type phù hợp.
7. Tại phần **Environment Variables**, thêm nếu cần:
   - `SECRET_KEY`: chuỗi bí mật riêng của anh
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: tên miền Render của dịch vụ, ví dụ `tccbdb-portal.onrender.com`
   - `CSRF_TRUSTED_ORIGINS`: `https://tccbdb-portal.onrender.com`
8. Bấm **Create Web Service**.

## 5) Tạo tài khoản admin sau khi deploy
Sau deploy đầu tiên, vào Render → **Shell** hoặc chạy local với cùng database rồi dùng:

```bash
python manage.py createsuperuser
```

Nếu anh dùng PostgreSQL trên Render thì nên chạy lệnh này trong Render Shell.

## 6) Về cơ sở dữ liệu
- Bản này hỗ trợ **SQLite khi chạy local**.
- Khi Render có biến môi trường `DATABASE_URL`, project sẽ tự dùng PostgreSQL.
- Nên dùng PostgreSQL cho site public.

## 7) Về ảnh/PDF upload trên admin
- File upload vào thư mục local sẽ **không bền vững trên Free web service**.
- Muốn giữ ảnh/PDF sau khi redeploy, anh nên dùng:
  - Render Persistent Disk (gói trả phí), hoặc
  - lưu file trên dịch vụ ngoài như Cloudinary / S3.

## 8) Cập nhật site sau này
Mỗi lần sửa code:

```bash
git add .
git commit -m "Cap nhat giao dien"
git push
```

Render sẽ tự deploy lại nếu bật auto-deploy.
