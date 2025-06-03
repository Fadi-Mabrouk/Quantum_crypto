from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SafeCode
from django.utils import timezone
from django.shortcuts import render
@csrf_exempt
def current_code(request):
    """Get or generate current code"""
    code = SafeCode.objects.filter(
        expires_at__gt=timezone.now(),
        is_used=False
    ).first() or SafeCode.generate_new()
    
    return JsonResponse({
        'code': code.code,
        'expires_in': (code.expires_at - timezone.now()).total_seconds(),
        'is_quantum': code.is_quantum
    })

@csrf_exempt
def verify_code(request):
    """Verify user-submitted code"""
    if request.method == 'POST':
        user_code = request.POST.get('code', '')
        is_valid = SafeCode.verify(user_code)
        return JsonResponse({'valid': is_valid})
    return JsonResponse({'error': 'POST required'}, status=400)

def home(request):
    return render(request, 'safeapi/index.html')

