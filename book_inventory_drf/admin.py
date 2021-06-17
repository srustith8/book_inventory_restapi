from django.contrib import admin

# Register your models here.
from .models import User,Book,CustomerOrder

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id','name','email','password']


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['book_id','book_name','author']

class CustomerOrderAdmin(admin.ModelAdmin):
    model = CustomerOrder
    list_display = ['login_name','booksborrowed','date']

admin.site.register(User,UserAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(CustomerOrder,CustomerOrderAdmin)