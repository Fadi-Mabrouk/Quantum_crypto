import requests
import json
from django.core.cache import cache
from django.conf import settings
import secrets

class QuantumRandomGenerator:
    """
    Uses ANU Quantum Random Numbers API with fallback to crypto RNG
    API Docs: https://qrng.anu.edu.au/contact/api-documentation/
    """
    
    @classmethod
    def get_quantum_random(cls, length=8):
        """Get true quantum random numbers"""
        try:
            response = requests.get(
                f'https://qrng.anu.edu.au/API/jsonI.php?length={length}&type=uint8',
                timeout=3  
            )
            data = json.loads(response.text)
            return data['data']
        except Exception as e:
            print(f"Quantum API failed: {e}")
            return cls._get_crypto_fallback(length)
    
    @staticmethod
    def _get_crypto_fallback(length):
        """Fallback to cryptographic random"""
        return [secrets.randbelow(256) for _ in range(length)]

    @classmethod
    def generate_code(cls, length=12):
        """Generate alphanumeric code from quantum/crypto random"""
        chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  
        random_bytes = cls.get_quantum_random(length)
        return ''.join(chars[b % len(chars)] for b in random_bytes)