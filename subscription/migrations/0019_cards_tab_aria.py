# Generated by Django 3.1.6 on 2021-08-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0018_cards_tab_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='tab_aria',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
