from django.db import models
from PIL import Image


class PaperKind(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Вид паперу')

    def __str__(self):
        return self.name


class PaperFormat(models.Model):
    name = models.CharField(max_length=50,verbose_name = 'Формат паперу')

    def __str__(self):
        return self.name


class PaperDensity(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Щільність паперу')

    def __str__(self):
        return (self.name)


class PaperWidth(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Ширина')

    def __str__(self):
        return (self.name)



class PaperHeight(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Висота')

    def __str__(self):
        return self.name


class PaperType(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Тип паперу')
    p_density = models.ManyToManyField(PaperDensity)

    def __str__(self):
        return self.name


class Product(models.Model):
    order_id = models.IntegerField(default=56, blank=True, null=True, verbose_name = '№')
    p_type =  models.ForeignKey(PaperType, on_delete=models.CASCADE)
    p_kind = models.ForeignKey(PaperKind, on_delete=models.CASCADE)
    p_density = models.ForeignKey(PaperDensity, on_delete=models.CASCADE)
    p_width = models.ForeignKey(PaperWidth,null=True, on_delete=models.CASCADE)
    p_format = models.ForeignKey(PaperFormat, null=True, on_delete=models.CASCADE)
    p_height = models.ForeignKey(PaperHeight,null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Оновлено')
    file = models.FileField(upload_to='Замовлення/%Y/%m/%d/', verbose_name = 'Посилання на макет')
    is_moved = models.BooleanField(default=True, verbose_name = 'Переміщено')

    def __str__(self):
        return f'{self.p_type.name} | {self.p_kind.name} | {self.p_width}х{self.p_height} мм | {self.p_format} | {self.p_density.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        ordering = ['-created_at']

