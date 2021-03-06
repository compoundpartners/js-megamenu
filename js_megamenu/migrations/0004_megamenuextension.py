# Generated by Django 2.2.13 on 2020-07-13 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('js_megamenu', '0003_section_attributes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MegamenuExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_megamenu', models.BooleanField(default=False, verbose_name='Show Megamenu Placeholder')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='js_megamenu.MegamenuExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
