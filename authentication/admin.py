from django.contrib import admin

from authentication.models import User

class BandAdmin(admin.ModelAdmin):
	list_display = ('username', 'role', 'first_name', 'is_active')

admin.site.register(User, BandAdmin)
