from django.contrib import admin

# Register your models here.
from .models import Domain,Xss,Xsspayload,Lfi,Lfipayload,Redirect


admin.site.register(Domain)
admin.site.register(Xss)
admin.site.register(Xsspayload)
admin.site.register(Lfi)
admin.site.register(Lfipayload)
admin.site.register(Redirect)