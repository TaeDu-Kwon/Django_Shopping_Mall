from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# 상품명, 모델 이름, 판매자 정보, 가격, 상품 설명

class Product_Info(models.Model):

    PRODUCT_CATEGORY = [
        ("Clothing","의류"),
        ("Beauty", "뷰티"),
        ("Food", "식품"),
        ("Kitchenware", "주방 용품"),
        ("Daily_Supplies", "생활 용품"),
        ("Electronic_devices","전자 기기"),
        ("Sports","스포츠 용품")
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 100, blank = False)
    model_name = models.CharField(max_length = 100, blank = True)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=1000,blank=True)
    product_image = models.ImageField(upload_to='product_info_images/')
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORY,blank=False)
    inventory = models.IntegerField()
    sold_out = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.product_name} - {self.category} - <{self.inventory}개 남음>"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.user.username}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product_Info, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}개"

    def total_price(self):
        return self.quantity * self.product.product_price