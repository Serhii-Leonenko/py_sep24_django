from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="children")

    class Meta:
        verbose_name_plural = "Children"

    def __str__(self):
        return self.name
