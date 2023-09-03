from django.db import models

class OrderListData(models.Model):
    PayTerms = models.CharField(max_length=200, verbose_name="支払条件")
    Status = models.CharField(max_length=200, verbose_name="ステータス")
    Supplier = models.CharField(max_length=200, verbose_name="発注先")
    WorkName = models.CharField(max_length=200, verbose_name="作品名")
    NumberEp = models.IntegerField(default=0,  verbose_name="話数")
    OrderDate = models.DateField(max_length=200, verbose_name="発注日")
    Money = models.IntegerField(default=0, verbose_name="金額")

    def __str__(self):
        return str(self.id)


class SupplierData(models.Model):
    Code = models.IntegerField(default=0,  verbose_name="発注先コード")
    Name = models.CharField(max_length=200, verbose_name="発注先名")

    def __str__(self):
        return str(self.Code)


class WorkNameData(models.Model):
    Code = models.IntegerField(default=0,  verbose_name="作品コード")
    Name = models.CharField(max_length=200, verbose_name="作品名")

    def __str__(self):
        return str(self.Code)

class NumberEpData(models.Model):
    Code = models.IntegerField(default=0,  verbose_name="話数コード")
    Name = models.CharField(max_length=200, verbose_name="話数名")

    def __str__(self):

        return str(self.Code)