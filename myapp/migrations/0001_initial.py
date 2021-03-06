# Generated by Django 3.2.3 on 2021-06-02 08:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=100)),
                ('cust_email', models.EmailField(max_length=200)),
                ('balance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('trans_id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.FloatField(default=0.0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever_set', to='myapp.customer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_set', to='myapp.customer')),
            ],
        ),
    ]
