# Generated by Django 4.2.4 on 2023-08-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_products_customer_datecreated'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=50, null=True)),
                ('price', models.FloatField(null=True)),
                ('quantity', models.IntegerField()),
                ('datecreated', models.DateField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='calc.tag'),
        ),
    ]
