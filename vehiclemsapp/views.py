from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Vehicle,VehicleQualityCheck
from .forms import *
import vehiclemsapp
# Create your views here.
def loginpage(request):
    if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'homepage.html')
            else:
                return HttpResponse('Invalid Credentials')
    else:
        return render(request, 'loginpage.html')   

def registerpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email= request.POST.get('email')
        password=request.POST.get('password')

        user= User.objects.create_user(username=username,email=email,password=password)
        return render(request, 'loginpage.html')
    else:
        return render(request, 'registerpage.html')


@login_required
def homepage(request):
    if request.method == 'POST':
        vehicle_num = request.POST.get('vehicle_number')
        vehicle_typ = request.POST.get('vehicle_type')
        del_chal_num = request.POST.get('delivery_challan_number')
        pur_ord_num = request.POST.get('purchase_order_number')

        # Assuming vehicle_num is unique, no need for the second query.
        try:
            vehicle=Vehicle.objects.get(vehicle_number=vehicle_num,vehicle_type=vehicle_typ, delivery_challan_number=del_chal_num,purchase_order_number=pur_ord_num)
            vehqc = VehicleQualityCheck.objects.get(vehicle=vehicle)
            return redirect(f"updatevehicle/{vehqc.pk}")
        except VehicleQualityCheck.DoesNotExist:
            return HttpResponse('Vehicle Not Found')

    else:
        # Handle the case for GET request or any other method.
        # You might want to render a form for the user to submit data.
        return render(request, 'homepage.html', {'vehicl=':None})

@login_required
def VehicleUpdate(request, pk):
    if request.method =='POST':
        v_c_b=request.POST.get('vehicle_checked_by')
        v_c_t=request.POST.get('vehiclechecktime')
        v_c_d=request.POST.get('vehiclecheckdate')
        v_i=request.POST.get('vehicle_inspection')
        if v_i=="on":
            v_i=True
        else:
            v_i=False
        v_r=request.POST.get('remarks')
        v_i_t=request.POST.get('isnpectiontype')
        v_i_d=request.POST.get('vehicle_inspection_details')
        v_c_a=request.POST.get('correctiveactions')
        v_q_c=VehicleQualityCheck.objects.get(pk=pk)
        v_q_c.checked_by=v_c_b
        v_q_c.check_time=v_c_t
        v_q_c.check_date=v_c_d
        v_q_c.inspection_passed=v_i
        v_q_c.remarks=v_r
        v_q_c.inspection_type=v_i_t
        v_q_c.inspection_details=v_i_d
        v_q_c.corrective_actions=v_c_a
        v_q_c.save()
        return HttpResponse('Vehicle Quality Checked Successfully')
    try:
        v_q_c=VehicleQualityCheck.objects.get(pk=pk)
        return render(request, 'updvehicle.html', {'vehicle_data':v_q_c})
    except VehicleQualityCheck.DoesNotExist:
        return HttpResponse("Vehicle Not Found")
