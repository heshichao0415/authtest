from django.contrib import admin
from product.models import Product
from apitest.models import Apitest, Apis
from apptest.models import Appcase             #用例管理功能前端开发
from webtest.models import Webcase
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    admin.site.register(Product)   #把产品模块注册到Django admin后台并能显示


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus',
                    'create_time', 'id', 'product']
    model = Apis
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'create_time', 'id']
    inlines = [ApisAdmin]


#用例管理功能前端开发
class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcasename', 'apptestresult', 'create_time', 'id', 'product']
    model = Appcase
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'create_time', 'id']
    inlines = [AppcaseAdmin]


#web用例管理功能后台开发
class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult', 'create_time', 'id', 'product']
    model = Webcase
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'create_time', 'id']
    inlines = [WebcaseAdmin]