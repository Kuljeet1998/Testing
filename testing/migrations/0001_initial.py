# Generated by Django 2.2 on 2020-08-25 07:54

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
            name='Staff',
            fields=[
                ('staff_no', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=35)),
                ('status', models.IntegerField(choices=[(0, 'pending'), (1, 'in_progress'), (2, 'Done')], default=0)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='testing.Staff')),
            ],
        ),
    ]
