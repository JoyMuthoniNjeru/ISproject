from django.db import models
from django.contrib.auth.models import User
from adminpanel.models import TestSlot

DRIVING_SCHOOLS = [
    ('AA Kenya', 'AA Kenya'),
    ('Seniors Driving School', 'Seniors Driving School'),
    ('Leopard Driving School', 'Leopard Driving School'),
    ('Hillys Driving School', 'Hillys Driving School'),
    ('Iqra Driving School', 'Iqra Driving School'),
    ('Sony Driving School', 'Sony Driving School'),
    ('Wings Driving School', 'Wings Driving School'),
    ('Budget Driving School', 'Budget Driving School'),
    ('Heltz Driving School', 'Heltz Driving School'),
    ('Petanns Driving School', 'Petanns Driving School'),
    ('Rocky Driving School', 'Rocky Driving School'),
    ('Jitegemea Driving School', 'Jitegemea Driving School'),
    ('Glory Driving School', 'Glory Driving School'),
    ('Top Gear Driving School', 'Top Gear Driving School'),
]

LICENSE_TYPES = [
    ('Class A', 'Class A'),
    ('Class B', 'Class B'),
    ('Class C', 'Class C'),
    ('Class F', 'Class F'),
    ('CDL', 'CDL'),
]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_slot = models.ForeignKey(TestSlot, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)
    pdl_number = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    country_of_residence = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    driving_school = models.CharField(max_length=50, choices=DRIVING_SCHOOLS)
    license_type = models.CharField(max_length=20, choices=LICENSE_TYPES)
    document_upload = models.FileField(upload_to='documents/')
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} – {self.test_slot}"

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('mpesa', 'M-Pesa'),
        ('airtel', 'Airtel Money'),
        ('visa', 'Visa'),
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    pin = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.full_name} – {self.payment_method} – {self.amount}"
