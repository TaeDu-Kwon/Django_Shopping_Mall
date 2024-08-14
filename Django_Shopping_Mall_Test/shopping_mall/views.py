from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from users.models import Profile
from .models import Product_Info,Cart,CartItem
from .forms import ProductAddForm,AddToCartForm

def main_page(request):
    user = request.user
    user_category = get_object_or_404(Profile, user = user)
    category_list = []
    current_list = []

    product_info = Product_Info.objects.all()
    
    for i in product_info:
        if i.category not in category_list:
            current_list.append(i)
            category_list.append(i.category)

    context = {
        "user_category" : user_category.category,
        "user" : user,
        "product_info" : product_info,
        "current_list" : current_list
    }
    return render(request,"shopping_mall/main_page.html",context)

def product_addition(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            product_info = form.save(commit=False)
            product_info.user = request.user  # 로그인한 사용자로 user 필드 설정
            product_info.save()
            return redirect("shopping_mall:main_page")
    else:
        form = ProductAddForm()
    
    return render(request,"shopping_mall/product_addition.html",{"form":form})

def category_page(request,category):

    category_info = Product_Info.objects.filter(category = category)

    return render(request,"shopping_mall/category_page.html",{"category_info":category_info})

def product_details(request,product_id):

    product_info = Product_Info.objects.get(pk = product_id)
    
    return render(request, "shopping_mall/product_details.html",{"product_info":product_info})


def cart(request):
    user_cart = get_object_or_404(Cart,user = request.user)
    cart_item = CartItem.objects.filter(cart = user_cart)
    user = request.user

    return render(request, "shopping_mall/cart.html",{"cart_item":cart_item,"user": user})


def handle_action(request,product_id):
    user_cart = get_object_or_404(Cart,user = request.user)
    cart_item_list = CartItem.objects.filter(cart = user_cart)
    user = request.user

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        action = request.POST.get('action')

        product = get_object_or_404(Product_Info, id=product_id)
        cart = get_object_or_404(Cart, user=request.user)

        # 장바구니에 동일한 상품이 있는지 확인
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity  # 동일 상품이 이미 있으면 수량 증가
        else:
            cart_item.quantity = quantity
        cart_item.save()
        
        if action == 'purchase':
            # 구매하기 로직 처리
            cart_item_list = CartItem.objects.get(pk = cart_item.id)
            user = request.user
            user_info = get_object_or_404(Profile, user = user)
            return render(request,"shopping_mall/bying_product.html",{"cart_item":cart_item_list,"user": user,"user_info":user_info})

        elif action == 'add_to_cart':
            
            return redirect('shopping_mall:main_page')
        
    return render(request, "shopping_mall/cart.html",{"cart_item":cart_item_list,"user": user})
   
def bying_product(request,product_id):
    user_cart = get_object_or_404(Cart,user = request.user)
    cart_item_list = CartItem.objects.get(pk = product_id)
    user = request.user
    user_info = get_object_or_404(Profile, user = user)

    return render(request,"shopping_mall/bying_product.html",{"cart_item":cart_item_list,"user": user,"user_info":user_info})

def cart_product_delete(request,product_id):
    user_cart = get_object_or_404(Cart,user = request.user)
    cart_item_list = CartItem.objects.filter(cart = user_cart)
    user = request.user
    
    get_cart_item = CartItem.objects.get(pk = product_id)
    get_cart_item.delete()

    return render(request, "shopping_mall/cart.html",{"cart_item":cart_item_list,"user": user})

def pay_product(request,product_id):
    get_cart_item = CartItem.objects.get(pk = product_id)
    user = request.user
    user_info = get_object_or_404(Profile, user = user)

    if request.method == 'POST':
        quantity = get_cart_item.quantity
        product_info = get_cart_item.product

        product = get_object_or_404(Product_Info, id=product_info.id)

        product.inventory -= quantity

        if product.inventory < quantity:
            return render(request,"shopping_mall/bying_product.html",{"cart_item":get_cart_item,"user": user,"user_info":user_info})

        if product.inventory <= 0:
            product.inventory = 0
            product.sold_out = True
        product.save()

        get_cart_item.delete()

        return redirect('shopping_mall:main_page')
    
    return render(request,"shopping_mall/bying_product.html",{"cart_item":get_cart_item,"user": user,"user_info":user_info})