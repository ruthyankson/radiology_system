from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required
def custom_admin_redirect(request):
    if request.user.is_superuser:
        return redirect(reverse('admin:index'))
    else:
        return redirect('all_staff:custom_dashboard')

def custom_dashboard(request):
    return render(request, 'pages/staff_base.html')
