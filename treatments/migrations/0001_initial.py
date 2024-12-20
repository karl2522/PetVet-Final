# Generated by Django 5.1.1 on 2024-12-07 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet_registration', '0001_initial'),
        ('registration_login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dosage_instructions', models.TextField()),
                ('side_effects', models.TextField(blank=True)),
                ('precautions', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.DurationField(help_text='Expected duration of the procedure')),
                ('preparation_instructions', models.TextField()),
                ('aftercare_instructions', models.TextField()),
                ('risks', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_type', models.CharField(choices=[('CHECKUP', 'Regular Checkup'), ('MEDICATION', 'Medication'), ('PROCEDURE', 'Procedure'), ('EMERGENCY', 'Emergency Visit')], default='CHECKUP', max_length=20)),
                ('status', models.CharField(choices=[('SCHEDULED', 'Scheduled'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='SCHEDULED', max_length=20)),
                ('scheduled_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('symptoms', models.TextField(blank=True, help_text='Symptoms observed during visit')),
                ('diagnosis', models.TextField(blank=True, help_text='Veterinary diagnosis')),
                ('treatment_plan', models.TextField(blank=True, help_text='Detailed treatment plan')),
                ('recommendations', models.TextField(blank=True, help_text='Additional recommendations for pet care')),
                ('next_visit', models.DateTimeField(blank=True, help_text='Recommended date for next visit', null=True)),
                ('dosage', models.CharField(blank=True, max_length=100)),
                ('frequency', models.CharField(blank=True, max_length=100)),
                ('duration', models.CharField(blank=True, max_length=100)),
                ('procedure_notes', models.TextField(blank=True)),
                ('complications', models.TextField(blank=True)),
                ('progress_notes', models.TextField(blank=True, help_text='Notes on treatment progress')),
                ('owner_notes', models.TextField(blank=True, help_text='Notes from pet owner')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('medication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='treatments.medication')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to='pet_registration.pet')),
                ('procedure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='treatments.procedure')),
                ('veterinarian', models.ForeignKey(limit_choices_to={'is_vet': True}, on_delete=django.db.models.deletion.CASCADE, to='registration_login.profile')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_type', models.CharField(choices=[('UPCOMING', 'Upcoming Treatment'), ('MISSED', 'Missed Treatment'), ('FOLLOWUP', 'Follow-up Required')], max_length=20)),
                ('reminder_date', models.DateTimeField()),
                ('message', models.TextField()),
                ('is_sent', models.BooleanField(default=False)),
                ('sent_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to='treatments.treatment')),
            ],
        ),
    ]
