from django.contrib import admin
from .models import Apartment, Street, House


class ApartmentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Apartment.objects.all()
        apartments = Apartment.objects.filter(user=request.user)

        return apartments

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            fields = super(ApartmentAdmin, self).get_fields(request, obj)
            for field in fields:
                yield field
        else:
            fields = super(ApartmentAdmin, self).get_fields(request, obj)
            for field in fields:
                if field == 'user':
                    continue
                yield field

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super(ApartmentAdmin, self).save_model(request, obj, form, change)
        else:
            obj.user = request.user
            obj.save()


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Street)
admin.site.register(House)
