
from __future__ import unicode_literals

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_slug', models.SlugField(default=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emt_c',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=50)),
                ('comp_slug', models.SlugField(default=None, unique=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(max_length=10)),
                ('package_cost', models.CharField(max_length=20)),
                ('package_services', models.CharField(max_length=100)),
                ('package_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.Category')),
                ('package_emt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.Emt_c')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_slug', models.SlugField(default=None, unique=True)),
            ],
        ),
    ]
