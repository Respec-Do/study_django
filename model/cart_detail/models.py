from django.db import models

from cart.models import Cart
from model.models import Period
from product.managers import ProductManager
from product.models import Product


class CartDetail(Period):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, default=1)
    # 게시중 0, 결제완료 1, 결제 삭제 -1 삭제 -2
    status = models.SmallIntegerField(null=False, default = 0)


    class Meta:
        db_table = 'tbl_cart_detail'
        ordering = ['-id']

