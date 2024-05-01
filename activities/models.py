from django.db import models

DAY_TYPE_CHOICES = [
    ("weekday", "weekday"),
    ("weekend", "weekend"),
    ("holiday", "holiday"),
    ("vacation", "vacation"),
]


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    insertion_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Rule(models.Model):
    name = models.ForeignKey(Activity, on_delete=models.CASCADE)
    reward = models.FloatField()
    punishment = models.FloatField()
    insertion_timestamp = models.DateTimeField(auto_now_add=True)


class Log(models.Model):
    activity = models.ForeignKey(Rule, on_delete=models.CASCADE)
    timestamp = models.DateField()
    insertion_timestamp = models.DateTimeField(auto_now_add=True)


class BaseValue(models.Model):
    day_type = models.CharField(
        max_length=100, choices=DAY_TYPE_CHOICES, default="weekday"
    )
    base = models.FloatField()
    insertion_timestamp = models.DateTimeField(auto_now_add=True)
