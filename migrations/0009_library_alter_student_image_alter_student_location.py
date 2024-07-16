# Generated by Django 5.0 on 2024-07-09 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_holiday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=255)),
                ('book_name', models.CharField(max_length=255)),
                ('book_language', models.CharField(choices=[('English', 'English'), ('Turkish', 'Turkish'), ('Chinese', 'Chinese'), ('Spanish', 'Spanish'), ('Arabic', 'Arabic')], max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('book_class', models.CharField(max_length=255)),
                ('book_type', models.CharField(choices=[('Book', 'Book'), ('DVD', 'DVD'), ('CD', 'CD'), ('Newspaper', 'Newspaper')], max_length=150)),
                ('book_status', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='students/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]