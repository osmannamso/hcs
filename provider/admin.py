from django.contrib import admin
from .models import Provider, Payment, Check
from house.models import Apartment


class CheckInline(admin.StackedInline):
    model = Check


class PaymentAdmin(admin.ModelAdmin):
    inlines = [CheckInline]

    def get_queryset(self, request):
        qs = super(PaymentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            provider = Provider.objects.get(user=request.user)
            return qs.filter(provider=provider)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            fields = super(PaymentAdmin, self).get_fields(request, obj)
            for field in fields:
                yield field
        else:
            fields = super(PaymentAdmin, self).get_fields(request, obj)
            for field in fields:
                if field == 'provider':
                    continue
                yield field

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super(PaymentAdmin, self).save_model(request, obj, form, change)
        else:
            provider = Provider.objects.get(user=request.user)
            obj.provider = provider
            obj.save()


class CheckAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(CheckAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(apartment__user=request.user)


admin.site.register(Provider)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Check)