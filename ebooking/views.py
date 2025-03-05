# from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse,HttpResponseRedirect
# from django.views.decorators.csrf import csrf_protect
# from .models import Booking

# # Create your views here.


# def index(request):
#     if request.method =="POST":
#         Name=request.POST.get('name')
#         Address=request.POST.get('address')
#         Phone=request.POST.get('P_number')
#         Email=request.POST.get('email')

#         EB = Booking()
#         EB.name = Name
#         EB.address = Address
#         EB.phone_number = Phone
#         EB.Email = Email
#         EB.save()

#     return render(request, 'index1.html')
#     # return HttpResponse("this is manisha rajput")


# def views_booking(request):
#     studentDetail = stu_reg.objects.all()
#     return render(request,'view.html',{'studentDetail':studentDetail})

# def delete_booking(request , student_id):
#     Booking_del = get_object_or_404(stu_reg, id=student_id)
#     Booking_del.delete()
#     return redirect('student_detail')

# def update_booking(request,student_id):
#     Student_del = get_object_or_404(stu_reg, id=student_id)
#     if request.method=="POST":
#         Student_del.fname = request.POST.get("FirstName")
#         Student_del.lname= request.POST.get("LastName")
#         Student_del.email= request.POST.get("Email")
#         Student_del.course= request.POST.get("Course")
#         # image= request.POST.get("Image")
#         # sign= request.POST.get("Sign")
#         Student_del.save()
#         return redirect('student_detail')
#     return render(request,'update.html',{'Student':Student_del})    


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Booking

# Function to handle the index page and form submission
def index(request):
    if request.method == "POST":  
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('P_number')
        email = request.POST.get('email')

        booking=Booking()
        booking.name = name
        booking.address = address
        booking.phone_number = phone
        booking.email = email
        booking.save()
    return render(request, 'index1.html')


def views_booking(request):
    booking_details = Booking.objects.all()
    return render(request, 'view.html', {'booking_details': booking_details})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('view')

def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.name = request.POST.get("Name")
        booking.address = request.POST.get("Address")
        booking.phone_number = request.POST.get("PhoneNumber")
        booking.email = request.POST.get("Email")
        booking.save()
        return redirect('view')

    return render(request, 'update.html', {'booking': booking})
