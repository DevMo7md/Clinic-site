# Generated by Django 5.0.1 on 2024-02-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clenicapp', '0004_delete_properties'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinec_site',
            name='details',
            field=models.CharField(default='notnull', help_text='تفاصيل عن طرق علاجها بالمركز', max_length=1000000),
        ),
    ]
