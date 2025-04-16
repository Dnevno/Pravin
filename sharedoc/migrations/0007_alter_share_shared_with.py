# Generated by Django 5.1.4 on 2025-04-16 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharedoc', '0006_alter_share_shared_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='shared_with',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_shares', to='sharedoc.userdata'),
        ),
    ]
