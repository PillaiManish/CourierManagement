from django.shortcuts import render,redirect
from .models import Courier_Tracking,Courier_Details
from django.contrib.auth.models import User,Group,auth
# Create your views here.
def f_homepage(request):
    return render(request,'homepage.html',)

def f_track(request):
    if request.method =='POST':
        consignment_no = request.POST['code_no']

        courier_info = Courier_Tracking.objects.filter(courier_id_id=consignment_no).order_by('-date_time')

        courier_detail = Courier_Details.objects.get(id=consignment_no)

        return render(request,'track.html',{'courier':courier_info,'details':courier_detail})

    return render(request,'track.html',)

def f_add(request):
    if request.user.is_authenticated and User.objects.filter(username=request.user, groups__name='Agents').exists() or User.objects.filter(username=request.user, groups__name='Dealers').exists():
        if request.method == 'POST':
            from_name = request.POST['from_name']
            from_address = request.POST['from_address']
            from_contact = request.POST['from_contact']

            to_name = request.POST['to_name']
            to_address = request.POST['to_address']
            to_contact = request.POST['to_contact']

            email = request.POST['to_email']
            parcel = request.POST['parcel_weight']
            
            new_courier = Courier_Details(from_name=from_name,from_address = from_address,from_contact=from_contact,to_name=to_name,to_address=to_address,to_contact=to_contact,to_email = email,parcel_weight=parcel)
            new_courier.save()

            current_courier = Courier_Details.objects.filter(from_name=from_name,from_address = from_address,from_contact=from_contact,to_name=to_name,to_address=to_address,to_contact=to_contact,to_email = email,parcel_weight=parcel).order_by('-id').first()
            return render(request,'add_detail.html',{'current':current_courier})    
        
        
        return render(request,'add_detail.html')
    else:
        return redirect('/')


def f_update(request):
    if request.user.is_authenticated and User.objects.filter(username=request.user, groups__name='Agents').exists():
        
        if request.method == 'POST':
            track_id = request.POST['id']
            place = request.user.username
            status = request.POST['status']
            remark = request.POST['remark']

            update_courier = Courier_Tracking(courier_id_id=track_id,place_id=place,status=status,remarks=remark)
            update_courier.save()

            return render(request,'update.html',{"msg":'Updated'})
    
        return render(request,'update.html',)

    
    
    else:
        return redirect('/')