from django.shortcuts import render,redirect
from .models import Attendee
from .forms import AttendeeForm
from datetime import datetime

def issuing(request):
    today = datetime.now()
    issue_date = "{}年{}月{}日".format(str(today.year),str(today.month).lstrip('0'),str(today.day).lstrip('0'))
    print(issue_date)
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            try:
                model = Attendee.objects.get(register_id=form.cleaned_data['register_id'])
                form.register_type = model.register_type
                form.issue_date = issue_date
                return render(request,'issuing/receipt.html',{'form':form})
            except:
                form.error = '受付番号が見つかりませんでした。'
                return render(request,'issuing/issuing.html',{'form':form})
    else:
        form = AttendeeForm()
    return render(request,'issuing/issuing.html',{'form':form })
