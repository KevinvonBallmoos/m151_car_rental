# Generated by Django 3.1.2 on 2020-10-24 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plz', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('ps', models.IntegerField()),
                ('details', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='cars')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='api.carlocation')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('street', models.CharField(max_length=25)),
                ('phone_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_code', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField()),
                ('rend', models.DateField(default=False)),
                ('is_picked_up', models.BooleanField(default=False)),
                ('is_returned', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car', models.ManyToManyField(to='api.Cars')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.location'),
        ),
    ]
