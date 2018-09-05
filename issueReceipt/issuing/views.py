from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from .models import Attendee
from .forms import AttendeeForm


def issuing(request):

    today = datetime.now()
    # 発行日
    issue_date = "{}年{}月{}日".format(
        str(today.year),
        str(today.month).lstrip('0'),
        str(today.day).lstrip('0'))
    # 但し書き用 PyCon JP yyyy
    pycon = "PyCon JP {} ".format(str(today.year))
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            try:
                model = Attendee.objects.get(
                    register_id=form.cleaned_data['register_id'],
                    register_name=form.cleaned_data['register_name'])
                form.register_type = model.register_type
                form.id = str(form.cleaned_data['register_id'])
                if model.register_type == "Business":
                    form.price = "15,000"
                if model.register_type == "Business (fees separately)":
                    form.price = "15,000"
                elif model.register_type == "Patron":
                    form.price = "40,000"
                elif model.register_type == "Tutorial":
                    form.price = "4,000"
                form.issue_date = issue_date
                form.pycon = pycon
                return render(request, 'issuing/receipt.html', {'form': form})
            except ObjectDoesNotExist:
                form.error = '入力された受付番号・connpass IDに該当する領収書が見つかりませんでした。'
                return render(request, 'issuing/issuing.html', {'form': form})
    else:
        form = AttendeeForm()
    return render(request, 'issuing/issuing.html', {'form': form})
