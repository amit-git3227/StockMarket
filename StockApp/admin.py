from django.contrib import admin

# Register your models here.
from StockApp.models import *


class StockUserAdmin(admin.ModelAdmin):
    list_display = ['username','full_name','mobile','is_active']

    class Meta:
         db_table = 'user_info'

class UserAuthTokensAdmin(admin.ModelAdmin):
    list_display = ['user_info','access_token','refresh_token','added_on','updated_on']

class UserQuerysAdmin(admin.ModelAdmin):
    list_display = ['name','user_name','query','added_on']


admin.site.register(StockUser,StockUserAdmin)
admin.site.register(UserAuthTokens,UserAuthTokensAdmin)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(UserQuerys,UserQuerysAdmin)
