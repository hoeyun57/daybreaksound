from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    part = models.CharField(max_length=30)

    email_verified = models.BooleanField(default=False)
    approval_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "승인 대기"),
            ("approved", "승인됨"),
            ("rejected", "거절됨"),
        ],
        default="pending",
    )
    role = models.CharField(
        max_length=20,
        choices=[
            ("member", "동아리원"),
            ("manager", "운영진")
        ],
        default="member",
    )
    email = models.EmailField(unique=True, blank=False)