from django.contrib import admin
from rent.models import*


admin.site.register(Customer)
# admin.site.register(VehicleType)
# admin.site.register(VehicleSize)
admin.site.register(Vehicle)

admin.site.register(RentalRate)
admin.site.register(Rental)




