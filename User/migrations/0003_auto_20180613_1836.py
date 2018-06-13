# Generated by Django 2.0.5 on 2018-06-13 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('User', '0002_auto_20180613_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercollection',
            name='books',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT,
                                    related_name='collection_users', to='Content.Book'),
        ),
        migrations.AlterField(
            model_name='usercollection',
            name='discussions',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT,
                                    related_name='collection_users', to='Discussion.Discuss'),
        ),
    ]