from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return User.objects.all()
        users = User.objects.filter(user=request.user)

        return users

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            fields = super(UserAdmin, self).get_fields(request, obj)
            for field in fields:
                yield field
        else:
            fields = super(UserAdmin, self).get_fields(request, obj)
            for field in fields:
                if field == 'user':
                    continue
                yield field

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super(UserAdmin, self).save_model(request, obj, form, change)
        else:
            obj.user = request.user
            obj.save()


admin.site.register(User, UserAdmin)
