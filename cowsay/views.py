from django.shortcuts import render

from cowsay.models import CowsText
from cowsay.forms import CowsTextForm
import subprocess

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CowsTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = CowsTextForm()
            cowsay_what = subprocess.run(
                ['cowsay'] + data['text'].split(), capture_output=True
            ).stdout.decode()
            CowsText.objects.create(
                text=data['text']
            )
            
        return render(request, 'index.html', {'cowsay_what': cowsay_what, 'form': form})

    form = CowsTextForm()
    return render(request, 'index.html', {'form': form})


def history(request):
    cowsay_list = list(CowsText.objects.all())
    most_recent = cowsay_list[-10:][::-1]

    return render(request, 'history.html', {'most_recent': most_recent})
