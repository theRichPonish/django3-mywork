from django.shortcuts import render
from django.shortcuts import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import *
from django.db import *
from django.contrib.auth import *
from .forms import *
from django.utils import timezone
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import *
def authentication(request):
    return redirect('signupuser')
def signinuser(request):
    if request.method=='GET':
        return render(request, 'authentication\signinuser.html', {'form':SignInUserForm(), 'title':'Sign In'})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'authentication\signinuser.html', {'form':SignInUserForm(), 'error': '''User not found or wrong Password. Pls try again. Thank You.''', 'title':'Sign In'})
        else:
            login(request, user)
            return redirect('currenttodos')
def signupuser(request):
    if request.method=='GET':
        return render(request, 'authentication\signupuser.html', {'form':SignUpUserForm(),'title':'Sign Up'})
    else:
        if request.POST['password'] == request.POST['confirm_password'] and request.POST['email'] == request.POST['confirm_email']:
            try:
                user = User.objects.create_user(request.POST['username'], email=request.POST['confirm_email'], password=request.POST['confirm_password'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'authentication\signupuser.html', {'form':SignUpUserForm(), 'error': '''User already exist pick a new username.''', 'title':'Sign Up'})
        else:
            return render(request, 'authentication\signupuser.html', {'form':SignUpUserForm(), 'error': '''Either Passwords or Emails didn't match.''', 'title':'Sign Up'})
@login_required
def signoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
@login_required
def userdetails(request):
    return render(request, r'authentication\userdetails.html', {'title':'Sign Up'})
@login_required
def changepassword(request):
    if request.method=='GET':
        form = ChangeThePasswordForm()
        good_stuff = {'form':form, 'title':'Change Password'}
        return render(request, 'authentication\changepassword.html', good_stuff)
    elif request.method=='POST':
        form = ChangeThePasswordForm()
        good_stuff = {'form':form, 'title':'Change Password'}
        user = authenticate(request, username=request.user, password=request.POST['current_password'])
        passwords_also_match = request.POST['new_password']==request.POST['confirm_new_password']
        if user is not None and passwords_also_match:
            u = User.objects.get(username__exact=request.user)
            u.set_password(request.POST['confirm_new_password'])
            u.save()
            login(request, u)
            return redirect('currenttodos')
        elif user is None and passwords_also_match:
            good_stuff.update({'error':'Wrong current password. Try Again.'})
            return render(request, 'authentication\changepassword.html', good_stuff)
        elif user is not None and not passwords_also_match:
            good_stuff.update({'error':'New passwords dont match. Try Again.'})
            return render(request, 'authentication\changepassword.html', good_stuff)
        elif user is None and not passwords_also_match:
            good_stuff.update({'error':"Wrong current password and New passwords also don't match. Try Again."})
            return render(request, 'authentication\changepassword.html', good_stuff)
        else:
            return HttpResponse('Yam')
    else:
        return HttpResponse('Yam')
