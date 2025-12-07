from django.db import models

# Create your models here.
STATUS_CHOICE = (
    ("activae", "Active"),
    ("off-duty", "Off-duty"),
    ("suspended", "Suspended"),
    ("terminated", "Teminated")
    
)

class Guard(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=13, unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="active")

    # Optional photo
    photo = models.ImageField(upload_to="guards/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Deployment(models.Model):
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.guard} → {self.client_name}"


class GuardContract(models.Model):
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE)
    contract_title = models.CharField(max_length=150)
    contract_file = models.FileField(upload_to="contracts/")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.contract_title} ({self.guard})"