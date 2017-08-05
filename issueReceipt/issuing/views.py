from django.shortcuts import render,redirect
from .models import Attendee
from .forms import AttendeeForm
from datetime import datetime

def issuing(request):
    today = datetime.now()
    issue_date = "{}年{}月{}日".format(str(today.year),str(today.month).lstrip('0'),str(today.day).lstrip('0'))
    pycon = "PyCon JP {} ".format(str(today.year))
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            try:
                model = Attendee.objects.get(register_id=form.cleaned_data['register_id'])
                form.register_type = model.register_type
                if model.register_type == "Business":
                    form.price = "15,000"
                elif model.register_type == "Patron":
                    form.price = "40,000"
                form.issue_date = issue_date
                form.pycon = pycon
                return render(request,'issuing/receipt.html',{'form':form})
            except:
                form.error = '受付番号が見つかりませんでした。'
                return render(request,'issuing/issuing.html',{'form':form})
    else:
        form = AttendeeForm()
    return render(request,'issuing/issuing.html',{'form':form })
