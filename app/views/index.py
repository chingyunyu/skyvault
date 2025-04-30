from django.shortcuts import render, redirect
from app.models.account import Account

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        email = request.POST.get('email')
        password = request.POST.get('password')
        level = request.POST.get('level')

        if action == 'signup':
            # Create account
            account, created = Account.objects.get_or_create(email=email)
            if created:
                account.password = password
                account.level = level
                account.save()
                # Redirect after signup
            else:
                # Account exists, maybe return error
                pass
        
        if action == 'signin':
            try:
                account = Account.objects.get(email=email, password=password)
            except Account.DoesNotExist:
                return redirect('/')  # Failed login
        
        # Login success
        if account.level == 'admin':
            return redirect('/admin')
        else:
            return redirect('/customer')
        
    return render(request, 'index.html')