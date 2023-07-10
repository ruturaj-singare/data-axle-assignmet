from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    parking_id = models.BigAutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.parking_id} | {self.pincode}"
    
class ParkingBooking(models.Model):
    VEHICLE_CHOICES = (
        ('2W', '2-Wheeler'),
        ('4W', '4-Wheeler'),
    )
    booking_id = models.BigAutoField(primary_key=True, null=False, blank=False)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE, related_name='parking_spot_related')
    vehicle_type = models.CharField(max_length=2, choices=VEHICLE_CHOICES, default='2W')
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.vehicle_type} Booking for Spot {self.parking_spot.parking_id}"

