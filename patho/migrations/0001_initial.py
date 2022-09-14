# Generated by Django 4.0.5 on 2022-09-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField()),
                ('case_id', models.IntegerField()),
                ('reporting_date', models.DateField()),
                ('patient_name', models.CharField(max_length=15)),
                ('reference_doctor', models.CharField(max_length=15)),
                ('amount', models.IntegerField()),
                ('paid_amount', models.IntegerField()),
                ('balance_amount', models.IntegerField()),
            ],
        ),
    ]