from django.db import models

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=100)
    delivery_challan_number = models.CharField(max_length=50)
    purchase_order_number = models.CharField(max_length=50)
    checked_out = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def _str_(self):
        return f"{self.vehicle_type} ({self.vehicle_number})"
    
    
    
class VehicleQualityCheck(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50)
    delivery_challan_number = models.CharField(max_length=50)
    checked_by = models.CharField(max_length=100)
    check_date = models.DateField()
    check_time = models.TimeField()
    inspection_passed = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)
    inspection_type = models.CharField(max_length=100)
    inspection_details = models.TextField(blank=True, null=True)
    defects_found = models.TextField(blank=True, null=True)
    corrective_actions = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Vehicle Quality Check'
        verbose_name_plural = 'Vehicle Quality Checks'

    def _str_(self):
        return f"{self.vehicle} - {self.check_date}"