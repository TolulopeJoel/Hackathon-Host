# Generated by Django 4.2.1 on 2023-05-12 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hackathon', '0002_hackathon_participants'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='submissions/files/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='submissions/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='hackathon.hackathon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]