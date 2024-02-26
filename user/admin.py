from django.contrib import admin
from .models import  *

# Register your models here.
class recentblogAdmin(admin.ModelAdmin):
    list_display = ('id','rbpic','rbday','rbmonth','rbname','rbncomm')
admin.site.register(recentblog,recentblogAdmin)

class teamAdmin(admin.ModelAdmin):
    list_display = ('id','tname','tpost','timg','theading')
admin.site.register(team,teamAdmin)

class eventAdmin(admin.ModelAdmin):
    list_display = ('id','eday','emonth','eyear','etime','eplace','ecity','epic')
admin.site.register(event,eventAdmin)

class registersAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Password','Contact','Picture','Address')
admin.site.register(registers,registersAdmin)

class detailAdmin(admin.ModelAdmin):
    list_display = ('name','mob','pic','address','gender','email','date')
admin.site.register(detail,detailAdmin)

class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Contact','Address','Message')
admin.site.register(contactus,contactusAdmin)

class aboutusAdmin(admin.ModelAdmin):
    list_display = ('user','exp','branch')
admin.site.register(aboutus,aboutusAdmin)

class neweventAdmin(admin.ModelAdmin):
    list_display = ('id','eday','emonth','eyear','etime','eplace','ecity','ehead','epic')
admin.site.register(newevent,neweventAdmin)

class thoughtAdmin(admin.ModelAdmin):
    list_display = ('para','pic','name','prof')
admin.site.register(thought,thoughtAdmin)

class footerAdmin(admin.ModelAdmin):
    list_display = ('fft','fst','sft','sst')
admin.site.register(footer,footerAdmin)