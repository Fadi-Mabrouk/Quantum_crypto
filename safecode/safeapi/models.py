from django.db import models
from django.utils import timezone
from .quantum import QuantumRandomGenerator
import string

class SafeCode(models.Model):
    code = models.CharField(max_length=12)
    generated_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    is_quantum = models.BooleanField(default=True)
    attempts = models.PositiveIntegerField(default=0)

    @classmethod
    def generate_new(cls):
        """Generate a new quantum or fallback code"""
        code = QuantumRandomGenerator.generate_code()
        is_quantum = not code.startswith('AAA')  
        
        return cls.objects.create(
            code=code,
            expires_at=timezone.now() + timezone.timedelta(seconds=30),
            is_quantum=is_quantum
        )

    @classmethod
    def verify(cls, user_code):
        current = cls.objects.filter(
            expires_at__gt=timezone.now(),
            is_used=False
        ).first()
        
        if not current:
            return False
            
        current.attempts += 1
        current.save()
        
        if current.code == user_code.upper():
            current.is_used = True
            current.save()
            return True
        return False


