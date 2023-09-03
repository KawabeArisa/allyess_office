from django.contrib import admin
from .models import OrderListData, SupplierData, WorkNameData, NumberEpData

class OrderListDataAdmin(admin.ModelAdmin):
    pass

class SupplierDataAdmin(admin.ModelAdmin):
    pass

class WorkNameDataAdmin(admin.ModelAdmin):
    pass

class NumberEpDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderListData, OrderListDataAdmin)
admin.site.register(SupplierData, SupplierDataAdmin)
admin.site.register(WorkNameData, WorkNameDataAdmin)
admin.site.register(NumberEpData, NumberEpDataAdmin)