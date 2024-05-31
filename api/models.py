from django.db import models

# Create your models here.
class User(models.Model):
    # Personal details
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # Training details
    joined_date = models.DateField(auto_now_add=True)

    # Progress tracking
    current_module = models.CharField(max_length=255, blank=True, null=True)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    # Status
    is_active = models.BooleanField(default=True)
    is_intern = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Trainuate User"
        verbose_name_plural = "Trainuate Users"


class UniversitySupervisor(models.Model):
    # Personal details
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # University details
    university_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)  # e.g., Professor, Dr., etc.


    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "University Supervisor"
        verbose_name_plural = "University Supervisors"


class CompanySupervisor(models.Model):
    # Personal details
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Company details
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)  # e.g., Manager, Senior Developer, etc.


    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.position} at {self.company_name}"

    class Meta:
        verbose_name = "Company Supervisor"
        verbose_name_plural = "Company Supervisors"