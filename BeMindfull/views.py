from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', { 'form': form })

def custom_register(request):
    if request.method == 'POST':
       form = UserCreationForm(data=request.POST)

       if form.is_valid():
           form.save()
           return redirect("/home")
    else:
        form = UserCreationForm()

    return render(request, "register.html", { 'form': form })
