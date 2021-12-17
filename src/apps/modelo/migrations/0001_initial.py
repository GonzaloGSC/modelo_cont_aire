# Generated by Django 3.2.10 on 2021-12-11 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modeloRespuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('p1', models.FloatField()),
                ('p2', models.FloatField()),
                ('p3', models.FloatField()),
                ('p4', models.FloatField()),
                ('p5', models.FloatField()),
                ('p6', models.FloatField()),
                ('p7', models.FloatField()),
                ('p8', models.FloatField()),
                ('p9', models.FloatField()),
                ('p10', models.FloatField()),
                ('p11', models.FloatField()),
                ('p12', models.FloatField()),
                ('p13', models.FloatField()),
                ('p14', models.FloatField()),
                ('p15', models.FloatField()),
                ('p16', models.FloatField()),
                ('p17', models.FloatField()),
                ('p18', models.FloatField()),
                ('p19', models.FloatField()),
                ('p20', models.FloatField()),
                ('p21', models.FloatField()),
                ('p22', models.FloatField()),
                ('p23', models.FloatField()),
                ('p24', models.FloatField()),
                ('p25', models.FloatField()),
                ('p26', models.FloatField()),
                ('p27', models.FloatField()),
                ('p28', models.FloatField()),
                ('p29', models.FloatField()),
                ('p30', models.FloatField()),
                ('i_d', models.FloatField()),
                ('i_m', models.FloatField()),
                ('i_y', models.FloatField()),
                ('i_aqi_max', models.FloatField()),
                ('i_aqi_mean', models.FloatField()),
                ('i_pm25', models.FloatField()),
                ('i_pm10', models.FloatField()),
                ('i_o3', models.FloatField()),
                ('i_no2', models.FloatField()),
                ('i_co', models.FloatField()),
                ('i_codigo_comuna', models.FloatField()),
            ],
        ),
    ]