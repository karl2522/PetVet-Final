# Generated by Django 5.1.1 on 2024-12-07 14:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(default='profile_pics/profile.png', upload_to='profile_pics/')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('preferred_payment', models.CharField(choices=[('CASH', 'Cash'), ('CARD', 'Credit/Debit Card'), ('GCASH', 'GCash'), ('MAYA', 'Maya')], default='CASH', max_length=10)),
                ('card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('card_expiry', models.CharField(blank=True, max_length=5, null=True)),
                ('ewallet_number', models.CharField(blank=True, max_length=15, null=True)),
                ('role', models.CharField(choices=[('OWNER', 'Pet Owner'), ('VET', 'Veterinarian')], default='OWNER', max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
