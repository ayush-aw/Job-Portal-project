# Generated by Django 2.0.5 on 2018-05-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applayjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=30)),
                ('MOBILE', models.CharField(max_length=15)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('RESUME', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CANDIDATE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=40)),
                ('MOBILENUMBER', models.CharField(max_length=20)),
                ('EMAILID', models.EmailField(max_length=254)),
                ('CREATEPASSWORD', models.CharField(max_length=20)),
                ('ADDRESS', models.CharField(max_length=200)),
                ('JOBINTERESTED', models.CharField(max_length=50)),
                ('QULIFICATION', models.CharField(max_length=20)),
                ('EXPERIENCE', models.CharField(max_length=10)),
                ('EXPECTEDSALARY', models.CharField(max_length=30)),
                ('CURRENTLOCATION', models.TextField()),
                ('PREFEREDLOCATION', models.TextField()),
                ('RESUME', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='COMPANY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COMPANYNAME', models.CharField(max_length=100)),
                ('ADDRESS', models.CharField(max_length=200)),
                ('CREATEPASSWORD', models.CharField(max_length=20)),
                ('STATE', models.CharField(max_length=50)),
                ('PINCODE', models.CharField(max_length=10)),
                ('COUNTRY', models.CharField(max_length=20)),
                ('EMAILID', models.EmailField(max_length=254)),
                ('LANDLINENUMBER', models.IntegerField()),
                ('MOBILENUMBER', models.IntegerField()),
                ('SECTOR', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CONSULTANT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CONSULTANTNAME', models.CharField(max_length=100)),
                ('ADDRESS', models.CharField(max_length=200)),
                ('CREATEPASSWORD', models.CharField(max_length=20)),
                ('STATE', models.CharField(max_length=50)),
                ('PINCODE', models.CharField(max_length=10)),
                ('COUNTRY', models.CharField(max_length=20)),
                ('EMAILID', models.EmailField(max_length=254)),
                ('LANDLINENUMBER', models.IntegerField()),
                ('MOBILENUMBER', models.IntegerField()),
                ('SECTOR', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JOBS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('POSTEDBY', models.CharField(choices=[('company', 'COMPANY'), ('consultant', 'CONSULTANT'), ('admin', 'ADMIN')], default='admin', max_length=20)),
                ('COMPANY', models.CharField(max_length=500)),
                ('LOCATION', models.CharField(max_length=900)),
                ('POST', models.CharField(max_length=100)),
                ('MINIMUMEXPERIENCE', models.CharField(max_length=120)),
                ('MINIMUMQUALIFICATION', models.CharField(max_length=120)),
                ('SALARYRANGE', models.CharField(max_length=100)),
                ('JOBDESCRIPTION', models.TextField(max_length=1000)),
                ('CONTACTPERSON', models.CharField(max_length=100)),
                ('MOBILE', models.CharField(max_length=20)),
                ('POSTDATE', models.DateField()),
                ('CURRENTSTATUS', models.CharField(choices=[('open', 'OPEN'), ('close', 'CLOSE'), ('select', 'SELECT')], default='select', max_length=30)),
                ('EMPLOYMENTTYPE', models.CharField(choices=[('full time', 'FULL TIME'), ('part time', 'PART TIME'), ('select', 'SELECT')], default='select', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]