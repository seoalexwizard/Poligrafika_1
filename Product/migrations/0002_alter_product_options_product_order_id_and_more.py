# Generated by Django 4.1.3 on 2022-11-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукти'},
        ),
        migrations.AddField(
            model_name='product',
            name='order_id',
            field=models.IntegerField(blank=True, default=56, null=True),
        ),
        migrations.AlterField(
            model_name='paperdensity',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Щільність паперу'),
        ),
        migrations.AlterField(
            model_name='paperformat',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Формат паперу'),
        ),
        migrations.AlterField(
            model_name='paperheight',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Висота'),
        ),
        migrations.AlterField(
            model_name='paperkind',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Вид паперу'),
        ),
        migrations.AlterField(
            model_name='papertype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Тип паперу'),
        ),
        migrations.AlterField(
            model_name='paperwidth',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(upload_to='Замовлення/%Y/%m/%d/', verbose_name='Посилання на макет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_moved',
            field=models.BooleanField(default=True, verbose_name='Переміщено'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
    ]
