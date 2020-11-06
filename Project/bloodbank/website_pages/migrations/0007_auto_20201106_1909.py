# Generated by Django 3.1.3 on 2020-11-06 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website_pages', '0006_blooddonationevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbank',
            name='BloodBankAdmin',
            field=models.ForeignKey(default='40', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
