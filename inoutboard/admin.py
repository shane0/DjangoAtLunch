from django.contrib import admin
from inout.inoutboard.models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id','name','last_mod','status','message',)
    list_filter = ('name',)


admin.site.register(Staff,StaffAdmin)
