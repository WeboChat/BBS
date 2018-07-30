# -*- coding: utf-8 -*-

from APP.forms import RegisterFrom
from APP.models import TieZi, UserModel


def create(request):
    if request.method == 'POST':
        print('zzz')
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = TieZi.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%s' % post.id)
    return render(request, 'create_post.html')


def read(request):
    post_id = int(request.GET.get('post_id'))

    post = TieZi.objects.get(id=post_id)
    return render(request, 'read_post.html',{'post': post})

def edit(request):
    if request.method == "POST":
        post_id = request.GET("post_id")
        post = TieZi.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get("content")
        post.save()
        return  redirect('/post/read/?post_id=%s'%post.id)
    else:
        post_id = int(request.GET('post_id'))
        post = TieZi.objects.get(id=post_id)
        return render(request, 'edit_post.html',{'post':post})

def search(request):
    keyword = request.POST.get('keyword')
    posts = TieZi.objects.get(keyword=keyword)
    return render(request, 'search.html', {'posts':posts})





def register(request):
    if request.method == "POST":
        form =RegisterFrom(request.POST, request.FILES)
        if form.is_valid:
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()

            request.session['uid'] = user.id
            return redirect('/user/info/')
        else:
            return render(request, 'register.html', {'error': form.errors})
    return render(request, 'register.html')


def login(request):
    user_id = request.GET.get('user_id')
    name = request.GET.get('name')
    password = request.GET.get('password')
    user = TieZi.objects.get(id=user_id)
    if request.session['uid'] == user.id:
        if name.exist:
            if check_password(password):
                return render(request, 'user_info.html', {'user': user})
        return redirect('/user/login/')
    else:
        return render(request, 'register.html', {})




def loginout(request):
    request.session.flush()
    return redirect('/user/login/')


def info(request):
    uid = request.session['uid']
    user = UserModel.objects.get(id=uid)
    return render(request, 'user_info.html', {'user': user})
