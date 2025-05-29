from django.contrib import admin

from main.models import Kindergarten, Region, Attendance, ChildRating, Child, ConsumedProduct, District, Group, \
    NoteOfHealth, Payment, Product


@admin.register(Kindergarten)
class KindergartenAdmin(admin.ModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass
@admin.register(Attendance)
class AttendancesAdmin(admin.ModelAdmin):
    pass

@admin.register(ChildRating)
class ChildRatingsAdmin(admin.ModelAdmin):
    pass

@admin.register(Child)
class ChildrenAdmin(admin.ModelAdmin):
    pass

@admin.register(ConsumedProduct)
class ConsumedProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(District)
class DistrictsAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    pass

@admin.register(NoteOfHealth)
class NoteOfHealthAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
