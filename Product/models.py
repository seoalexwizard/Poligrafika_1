from django.db import models


class PaperKind(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PaperFormat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PaperDensity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)

class PaperWidth(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)

class PaperHeight(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PaperType(models.Model):
    name = models.CharField(max_length=50)
    p_density = models.ManyToManyField(PaperDensity)


    def __str__(self):
        return self.name


class Product(models.Model):
    order_id = models.IntegerField
    p_type =  models.ForeignKey(PaperType, on_delete=models.CASCADE)
    p_kind = models.ForeignKey(PaperKind, on_delete=models.CASCADE)
    p_density = models.ForeignKey(PaperDensity, on_delete=models.CASCADE)
    p_width = models.ForeignKey(PaperWidth,null=True, on_delete=models.CASCADE)
    p_format = models.ForeignKey(PaperFormat, null=True, on_delete=models.CASCADE)
    p_height = models.ForeignKey(PaperHeight,null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='Замовлення/%Y/%m/%d/')
    is_moved = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.p_type.name} | {self.p_kind.name} | {self.p_width}х{self.p_height} мм | {self.p_format} | {self.p_density.name}'