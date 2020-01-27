from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='이름')
    tel = models.CharField(max_length=20, verbose_name='전화번호')
    address = models.CharField(max_length=200, verbose_name='주소')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=50, verbose_name='제품명')
    photo = models.ImageField(upload_to="", blank=True, verbose_name='제품 사진')
    desc = models.TextField(verbose_name='제품 설명')
    price = models.PositiveIntegerField(verbose_name='가격')
    stock = models.IntegerField(default=0, verbose_name='남은 수량')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='거래처')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:inventory-detail', kwargs={'pk': self.pk})
