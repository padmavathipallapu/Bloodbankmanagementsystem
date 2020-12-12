# Generated by Django 3.1.3 on 2020-12-12 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('G', 'Government'), ('R', 'Red Cross'), ('C', 'Charitable'), ('P', 'Private')], max_length=15)),
                ('contactNo', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('PostalAddress', models.CharField(max_length=100)),
                ('BloodBankAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packetID', models.CharField(max_length=25)),
                ('amount', models.FloatField()),
                ('bloodBank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website_pages.bloodbank')),
                ('boughtBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bloodBank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website_pages.bloodbank')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BloodPacket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packetID', models.CharField(max_length=70)),
                ('bloodGroup', models.CharField(choices=[('1', 'A+'), ('2', 'A-'), ('3', 'B+'), ('4', 'B-'), ('5', 'AB+'), ('6', 'AB-'), ('7', 'O+'), ('8', 'O-')], max_length=3)),
                ('expiryDate', models.DateField()),
                ('quantity', models.IntegerField(default=250)),
                ('price', models.FloatField(default=500.0)),
                ('Blood_bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website_pages.bloodbank')),
            ],
        ),
        migrations.CreateModel(
            name='BloodDonationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=70)),
                ('time', models.CharField(max_length=70)),
                ('campName', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
                ('district', models.CharField(max_length=70)),
                ('contactNo', models.CharField(max_length=15)),
                ('organizedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website_pages.bloodbank')),
            ],
        ),
        migrations.AddField(
            model_name='bloodbank',
            name='BloodPackets',
            field=models.ManyToManyField(blank=True, to='website_pages.BloodPacket'),
        ),
    ]
