# Generated manually for project update on 2026-04-07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_organizationunit_alter_leadershipmember_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulletinIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('bulletin_type', models.CharField(choices=[('month', 'Bản tin tháng'), ('season', 'Bản tin mùa'), ('year', 'Bản tin năm'), ('special', 'Chuyên đề')], default='month', max_length=20)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('period_label', models.CharField(blank=True, help_text='Ví dụ: Tháng 3/2026, Mùa khô 2026, Năm 2025...', max_length=120)),
                ('summary', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='bulletins/')),
                ('file', models.FileField(blank=True, null=True, upload_to='bulletins/files/')),
                ('published_at', models.DateField()),
                ('is_published', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Bản tin',
                'verbose_name_plural': 'Bản tin',
                'ordering': ['order', '-published_at', 'title'],
            },
        ),
        migrations.CreateModel(
            name='LeadershipAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('supporting_text', models.CharField(blank=True, help_text='Ví dụ: Phối hợp cùng các Phó Giám đốc hoặc các phòng liên quan', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignments', to='core.leadershipmember')),
            ],
            options={
                'verbose_name': 'Mảng lãnh đạo phụ trách',
                'verbose_name_plural': 'Mảng lãnh đạo phụ trách',
                'ordering': ['order', 'title'],
            },
        ),
    ]
