# Generated by Django 4.1.4 on 2022-12-12 08:06

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('registered_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CameraImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.models.CameraImage.get_camera_image_path)),
                ('taken_at', models.DateTimeField(auto_now=True)),
                ('camera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.camera')),
            ],
            options={
                'ordering': ['-taken_at'],
            },
        ),
    ]
