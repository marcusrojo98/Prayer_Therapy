from django.db import models

class PrayerTopic(models.Model):
    title = models.CharField(max_length=255)
    confession = models.TextField()

    def __str__(self):
        return self.title

class Prayer(models.Model):
    topic = models.ForeignKey(PrayerTopic, related_name='prayers', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    
    def __str__(self):
        return self.title

from django.db import models

class Donation(models.Model):
    # Donor Information
    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField()
    
    # Donation Details
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)
    
    # Payment Status (you can use this to track the payment status if you want)
    payment_status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Donation by {self.donor_name} - ${self.amount} on {self.donation_date}"
