# Generated by Django 4.2.11 on 2024-03-14 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NavelOrangeWorm', '0002_remove_event_id_event_cmsplugin_ptr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventlink',
            name='event',
        ),
        migrations.AddField(
            model_name='eventlink',
            name='plugin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='associated_item', to='NavelOrangeWorm.event'),
            preserve_default=False,
        ),
    ]
