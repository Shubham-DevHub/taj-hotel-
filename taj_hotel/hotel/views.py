from django.shortcuts import render, redirect
from .forms import BookingForm, ContactForm
import uuid
from datetime import date

def home(request):
    return render(request, 'hotel/home.html')

def rooms(request):
    return render(request, 'hotel/rooms.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'hotel/thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'hotel/contact.html', {'form': form})

def about(request):
    return render(request, 'hotel/about.html')



def book_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        room_type = request.POST.get('room_type')
        guests = request.POST.get('guests')
        requests_note = request.POST.get('requests')

        # Calculate pricing
        base_price = {
            'Deluxe Room': 150,
            'Luxury Suite': 250,
            'Ocean View': 300,
            'Presidential Suite': 500,
        }

        room_rate = base_price.get(room_type, 100)
        tax = round(room_rate * 0.12, 2)
        total = round(room_rate + tax, 2)

        # Generate booking ID
        booking_id = str(uuid.uuid4())[:8].upper()

        context = {
            'name': name,
            'email': email,
            'check_in': check_in,
            'check_out': check_out,
            'room_type': room_type,
            'guests': guests,
            'requests': requests_note,
            'room_rate': room_rate,
            'tax': tax,
            'total': total,
            'booking_id': booking_id,
            'today_date': date.today()
        }

        return render(request, 'hotel/booking_success.html', context)

    return render(request, 'hotel/booking.html')  # GET request shows form

def booking_success(request):
    return render(request, 'hotel/booking_success.html')


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'hotel/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'hotel/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')








