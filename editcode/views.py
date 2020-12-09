from django.shortcuts import render, redirect
from editcode.models import *
from django.utils.http import urlencode
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    if not request.session.get('username'):
        message = request.GET.get('message')
        print(message)
        return render(request, 'signup_login.html', {
            'message': message
        })
    else:
        return user_page(request)

def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.filter(username__exact=username).first()
    
    if user:
        request.session['username'] = username
        return redirect('/')
    else:
        return redirect('/?{}'.format(urlencode({
            'message': 'Wrong credentials!'
        })))

def sign_up(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.filter(username__exact=username, password__exact=password).first()
    
    if user:
        return redirect('/?{}'.format(urlencode({
            'message': 'User already exists!'
        })))
    
    user = User(username=username, password=password)
    user.save()

    return redirect('/?{}'.format(urlencode({
            'message': 'User created!'
        })))

def user_page(request):
    username = request.session['username']
    print(username, "HEEHEHEHEH")
    user = User.objects.filter(username__exact=request.session['username']).first()
    codes = Code.objects.filter(user__exact=user)
    if not codes:
        codes = []
    return render(request, 'user_page.html', {
        'username': username,
        'codes': codes
    }) 

def view_file(request):
    user = User.objects.filter(username__exact=request.session['username']).first()
    code = Code.objects.filter(user__exact=user, id__exact=int(request.GET['id'])).first()
    if not code:
        return HttpResponse('File not authorized or does not exist!')
    return render(request, 'view_page.html', {
        'code': code
    })

def delete_file(request):
    user = User.objects.filter(username__exact=request.session['username']).first()
    code = Code.objects.filter(user__exact=user, id__exact=request.GET['id']).first()
    if not code:
        return HttpResponse('File not authorized or does not exist!')
    code.delete()
    return redirect('/')

def save_file(request):
    code_id = request.POST['id']
    print(request.POST)
    username = request.session['username']
    user = User.objects.filter(username__exact=username).first()

    code = Code.objects.filter(user__exact=user, id__exact=code_id).first()
    code.text = request.POST['code']
    code.save()
    return redirect('/')

def new_file(request):
    user = User.objects.filter(username__exact=request.session['username']).first()
    code = Code.objects.filter(user__exact=user, type__exact=request.POST['type'], file_name__exact=request.POST['file_name']).first()
    if code:
        return redirect('/')

    code = Code(user=user, text="", type=request.POST['type'], file_name=request.POST["file_name"])
    code.save()
    print(code.id, "CHU")
    return redirect('/view/?id='.format(str(code.id)))
