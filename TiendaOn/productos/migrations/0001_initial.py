# Generated by Django 2.2.4 on 2019-08-26 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('ubicacion', models.CharField(max_length=120)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('precio', models.FloatField()),
                ('costo_envio', models.FloatField()),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='productos.Proveedor')),
            ],
        ),
    ]
