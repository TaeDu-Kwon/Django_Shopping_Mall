from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Product_Info,CartItem

class ProductAddForm(forms.ModelForm):

    PRODUCT_CATEGORY = [
        ("Clothing","의류"),
        ("Beauty", "뷰티"),
        ("Food", "식품"),
        ("Kitchenware", "주방 용품"),
        ("Daily_Supplies", "생활 용품"),
        ("Electronic_devices","전자 기기"),
        ("Sports","스포츠 용품")
    ]

    product_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'product-control'}))
    model_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'product-control'}))
    product_price = forms.IntegerField()
    product_description = forms.CharField(label="상품 설명", widget=forms.Textarea(attrs={
        'rows':10,
        'cols' : 135,
        'class': 'product-control',
        'placeholder':'내용을 입력하세요',
    }))
    product_image = forms.ImageField()
    category = forms.ChoiceField(choices=PRODUCT_CATEGORY, widget=forms.Select(attrs={'class': 'product-control', 'style': 'font-size: 16px; width: 300px;'}))

    class Meta:
        model = Product_Info
        fields = ['product_name','model_name','product_price','product_description','product_image',"category"]


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']