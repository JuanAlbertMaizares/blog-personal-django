from django.contrib import admin 
from applications.home.models import Home, Contact, Suscribers

# Register your models here.
admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(Suscribers)