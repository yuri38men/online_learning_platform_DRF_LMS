# Generated by Django 4.2.6 on 2023-10-22 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата оплаты')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('transfer', 'перевод на счет')], default='cash', max_length=20, verbose_name='способ оплаты')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='оплаченный курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.lesson', verbose_name='оплаченный урок')),
            ],
            options={
                'verbose_name': 'платёж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]