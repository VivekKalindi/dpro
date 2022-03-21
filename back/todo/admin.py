from django.contrib import admin

# Register your models here.

# import model Todo
from .models import Todo
 
# create a class for the admin-model integration
class TodoAdmin(admin.ModelAdmin):
 
    #  fields of the model here
    list_display = ("title","description","completed")
 
# to register the
# model class and the Admin model class
# using register() method
# of admin.site class
admin.site.register(Todo,TodoAdmin)