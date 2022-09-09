from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from talent.models import signup
from talent.models import talent_uploads
from talent.models import comment
from talent.models import rating


def index(request):
    return render(request, 'talent/index-business.html')


# Create your views here.
def signup1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('pass')
        role = request.POST.get('role')

        obj = signup()
        obj.name = name
        obj.email = email
        obj.mobile = mobile
        obj.password = password
        obj.role = role
        obj.save()
    return render(request, 'talent/index-business.html')


def login(request):
    obj = signup()
    email = request.POST.get('email')
    name = request.POST.get('name')
    password = request.POST.get('password')

    user = signup.objects.filter(email=email, password=password, status=1)

    if user.count() == 0:
        dic = {'msg': 'Invalid user name or password'}
        return render(request, 'talent/index-business.html', context=dic)
    else:
        data = signup.objects.get(email=email, password=password, status=1)
        username = name
        request.session['username'] = email
        request.session['role'] = data.role
        request.session['id'] = data.id

        dic = {'data': data}
        return render(request, 'talent/index-business.html', dic)


def logout(request):
    request.session.flush()
    return render(request, 'talent/index-business.html')


def up_files(request):
    return render(request, 'talent/upload_talent.html')


def file_save(request):
    ob = talent_uploads()
    id = signup.objects.get(id=request.POST.get('id'))
    type = request.POST.get('type')
    title = request.POST.get('title')

    desc = request.POST.get('desc1')

    myfile = request.FILES['fileinput']
    str1 = str(myfile)
    st = str1.split(".")

    if st[1] == 'mp4' or st[1] == 'jpg' or st[1] == 'png':
        ob.can_id = id
        ob.desc = desc
        ob.type = type
        ob.title = title
        ob.files = myfile
        ob.save()
        return HttpResponse("<script>alert('Saved Successfully');window.location='../talent/up_files';</script>")
        # return render(request, 'talent/upload_talent.html')
    else:

        dic = {'msg': 'This file type is not supported'}
        return render(request, 'talent/upload_talent.html', dic)


def view_talents(request):
    talents = talent_uploads.objects.all()

    commentss = comment.objects.all()

    ratings = rating.objects.all()
    sign = signup.objects.get(id=request.session['id'])
    talent_dict = {'tal': talents, 'comments': commentss, 'rating': ratings, 'sign': sign}

    return render(request, 'talent/talents.html', context=talent_dict)


def comment_save(request):
    com = comment()
    id = request.POST.get('id')
    user_id = signup.objects.get(id=request.POST.get('id'))

    tid = request.POST.get('tid')

    comments = request.POST.get('comment')
    com.user_id_id = user_id.id
    com.talent_id_id = tid
    com.name = user_id.name
    com.comment = comments

    com.save()
    talents = talent_uploads.objects.all()
    commentss = comment.objects.all()
    ratings = comment.objects.all()
    sign = signup.objects.get(id=request.session['id'])
    talent_dict = {'tal': talents, 'comments': commentss, 'rating': ratings, 'sign': sign}
    return render(request, 'talent/talents.html', context=talent_dict)


def rating_save(request):
    com = rating()
    id = request.POST.get('id')
    user_id = signup.objects.get(id=request.POST.get('id'))
    tid = request.POST.get('tid')

    ratings = request.POST.get('rating')
    com.user_id_id = user_id.id
    com.talent_id_id = tid
    com.rating = ratings

    com.save()
    talents = talent_uploads.objects.all()
    commentss = comment.objects.all()

    ratings = rating.objects.all()
    talent_dict = {'tal': talents, 'comments': commentss, 'rating': ratings}
    return render(request, 'talent/talents.html', context=talent_dict)


def gallery(request):
    return render(request, 'talent/gallery.html')


def contact(request, id):
    con = talent_uploads.objects.get(id=id)
    c = signup.objects.get(id=con.can_id_id)
    talent_d = {'contact': c}
    return render(request, 'talent/contact.html', context=talent_d)


def edit(request, id):
    talents = talent_uploads.objects.get(id=id)
    talent_dict = {'tal': talents}
    return render(request, 'talent/edit_talent.html', context=talent_dict)


def updateProfile(request, id):
    if request.method == 'POST':
        profile = talent_uploads.objects.get(id=id)
        type = request.POST.get('type')
        title = request.POST.get('title')
        desc = request.POST.get('desc1')
        myfile = request.FILES['photo']

        profile.type = type
        profile.title = title
        profile.desc = desc
        profile.files = myfile
        profile.save()
        talents = talent_uploads.objects.all()
        commentss = comment.objects.all()
        ratings = rating.objects.all()
        sign = signup.objects.get(id=request.session['id'])
        talent_dict = {'tal': talents, 'comments': commentss, 'rating': ratings, 'sign': sign}

        return render(request, 'talent/talentedit.html', context=talent_dict)
    else:
        profile = talent_uploads.objects.get(id=id)
        return render(request, 'talent/edit_talent.html', {'tal': profile})


def deletetalent(request, id):
    dist = talent_uploads.objects.get(id=id)
    dist.delete()
    talents = talent_uploads.objects.all()
    commentss = comment.objects.all()
    ratings = comment.objects.all()
    talent_dict = {'tal': talents, 'comments': commentss, 'rating': ratings}
    return render(request, 'talent/talents.html', talent_dict)


def profile(request):
    prof = signup.objects.get(id=request.session['id'])
    return render(request, 'talent/candidate_profile.html', {'prof': prof})


def admin(request):
    return render(request, 'talent/admin.html')


def approve(request):
    userid = request.session.get('id')
    reg = signup.objects.all()
    # login = signup.objects.all()
    context = {'reg': reg}
    return render(request, 'talent/approve.html', context)


def accept(request, id):
    aid = signup.objects.get(id=id)
    aid.status = 1
    aid.save()
    return HttpResponseRedirect('../approve')


def block(request, id):
    login = signup.objects.get(id=id)
    # status = request.session.get('status')
    login.status = 0
    login.save()
    return HttpResponseRedirect('../approve')


def talentview(request):
    userid = request.session.get('id')
    re = talent_uploads.objects.all()
    context = {'re': re}
    return render(request, 'talent/talentview.html', context)


def delete(request, id):
    dist = talent_uploads.objects.get(id=id)
    dist.delete()
    re = talent_uploads.objects.all()
    context = {'re': re}
    return render(request, 'talent/talentview.html', context)


def delcom(request, id):
    d = comment.objects.get(id=id)
    d.delete()
    talents = talent_uploads.objects.all()
    commentss = comment.objects.all()
    ratings = comment.objects.all()
    sign = signup.objects.get(id=request.session['id'])
    talent_dict = {'tal': talents, 'comments': commentss, 'rating': ratings, 'sign': sign}
    return render(request, 'talent/talents.html', context=talent_dict)


def delcomm(request, id):
    de = comment.objects.get(id=id)
    de.delete()
    talents = talent_uploads.objects.all()
    commentss = comment.objects.all()
    ratings = rating.objects.all()
    sign = signup.objects.get(id=request.session['id'])
    talent_dict = {'tal': talents, 'comments': commentss, 'rating': ratings, 'sign': sign}

    return render(request, 'talent/talentedit.html', context=talent_dict)


def tedit(request):
    talents = talent_uploads.objects.all()

    commentss = comment.objects.all()

    ratings = rating.objects.all()
    sign = signup.objects.get(id=request.session['id'])
    talent_dict = {'tal': talents, 'comments': commentss, 'rating': ratings, 'sign': sign}

    return render(request, 'talent/talentedit.html', context=talent_dict)


def editp(request, id):
    si = signup.objects.get(id=id)
    sign_dict = {'sig': si}
    return render(request, 'talent/edit_signup.html', context=sign_dict)


def updatep(request, id):
    if request.method == 'POST':
        pro = signup.objects.get(id=id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        pro.name = name
        pro.email = email
        pro.mobile = mobile
        pro.password = password
        pro.save()

        prof = signup.objects.get(id=request.session['id'])
        return render(request, 'talent/candidate_profile.html', {'prof': prof})
    else:
        si = signup.objects.get(id=id)
        sign_dict = {'sig': si}
        return render(request, 'talent/edit_signup.html', context=sign_dict)


def deletep(request, id):
    di = signup.objects.get(id=id)
    di.delete()
    request.session.flush()
    return HttpResponse("<script>alert('Your account is deleted..');window.location='../../talent';</script>")




