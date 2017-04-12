from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.forms.formsets import formset_factory

from .forms import CalForm
from .forms import ResultForm

from .LiFFT_compute import MyApp
# Create your views here.


def index(request):
    # if this is a POST request we need to process the form data

    num_task = 5
    damage, percent, moment = [], [], []
    for i in range(num_task):
        moment.append(0)
        damage.append(0)
        percent.append(0)
    total_risk = 0

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_set_new = formset_factory(CalForm, extra=num_task)
        form_set = form_set_new(request.POST)

        # check whether it's valid:
        if form_set.is_valid():
            data = form_set.data.copy()

            for i in range(num_task):
                lever_arm = float(data['form-'+str(i)+'-distance'])
                load = float(data['form-'+str(i)+'-load'])
                rep = float(data['form-'+str(i)+'-rep'])

                LiFFT_cal = MyApp(lever_arm, load, rep)
                moment[i], damage[i] = LiFFT_cal.cal()

            total_damage = sum(damage)
            if total_damage != 0:
                for j in range(len(damage)):
                    percent[j] = round(damage[j]/total_damage*100, 1)

            total_risk = LiFFT_cal.damage_to_risk(total_damage)






            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return render(request, 'ErgoTool/ErgoTool_Results.html')
            print (damage)
        else:
            print("Error")

    # if a GET (or any other method) we'll create a blank form
    else:
        form_set = formset_factory(CalForm, extra=num_task)


    return render(request, 'ErgoTool/ErgoTool_Header.html',
                  {'task_range':range(num_task), 'form_set': form_set,
                   'moment':moment, 'damage': damage, 'percent': percent,
                   'total_risk': total_risk})

'''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CalForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.data.copy()

            damage_value = form.cleaned_data['load'] + form.cleaned_data['rep']
            damage["0"] = damage_value
            form = CalForm(data)

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return render(request, 'ErgoTool/ErgoTool_Results.html')
        else:
            print ("Error")
           
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CalForm()
    return render(request, 'ErgoTool/ErgoTool_Header.html',
                  {'form': form, 'damage':damage, 'risk':risk})

    # return render_to_response('ErgoTool/ErgoTool_Header.html')
    # return render(request, 'ErgoTool/ErgoTool_Header.html')
'''

