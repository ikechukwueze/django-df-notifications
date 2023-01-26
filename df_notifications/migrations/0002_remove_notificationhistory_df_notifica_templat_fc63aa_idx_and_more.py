# Generated by Django 4.1.5 on 2023-01-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_notifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='notificationhistory',
            name='df_notifica_templat_fc63aa_idx',
        ),
        migrations.RenameField(
            model_name='notificationhistory',
            old_name='template_prefix',
            new_name='template',
        ),
        migrations.AddIndex(
            model_name='notificationhistory',
            index=models.Index(fields=['template', 'created'], name='df_notifica_templat_ec4b48_idx'),
        ),
    ]
