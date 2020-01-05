from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
from django.contrib import messages
import datetime
import time
import json
names=""
def index(request):
    if request.method=="POST":
        un = request.POST.get("username", None)
        pw = request.POST.get("password", None)
        molu = models.User.objects.all()
        for i in range(len(molu)):
            if (molu[i].username==str(un) and molu[i].password==str(pw)):
                if molu[i].username=="yang":
                    dictx=[]
                    dicty=[]
                    name=[]
                    for w in ["ag 白银","pb 铅"]:
                        x,y=catchin(5,w)
                        dictx.append(x)
                        dicty.append(y)
                        name.append(w)
                    return render(request, "manage.html",{"dx":json.dumps(dictx),"dy":json.dumps(dicty),"dn":json.dumps(name)})
                dict = []
                datafor2 = models.Infss.objects.all()
                for j in range(len(datafor2)):
                    if (datafor2[j].trans == str(molu[i].username)):
                        temp = {'time': datafor2[j].timenows, 'id': str(datafor2[j].id), 'ids': datafor2[j].ids,
                                'score': datafor2[j].score}
                        dict.append(temp)
                return render(request, "loginsuc.html",{"name":molu[i].username,"dic":dict,"t":datetime.date.today()})
    return render(request,"index.html")
def input(request):
    if request.method=="POST":
        if 'trainss' in request.POST:
            names = request.POST.get("trainss", None)
            cat = request.POST.get("cat", None)
            sco = request.POST.get("sco", None)
            pt = request.POST.get("ptime", None)
            ps = request.POST.get("psco", None)
            re= request.POST.get("remark", None)
            mol=models.Infss(trans=names,ids=cat,score=sco,ptime=pt,psco=ps,remarks=re)
            mol.save()
            dict = []
            datafor = models.Infss.objects.all()
            for i in range(len(datafor)):
                if (datafor[i].trans == str(names)):
                    temp = {'time': datafor[i].timenows, 'id': str(datafor[i].id), 'ids': datafor[i].ids, 'score': datafor[i].score}

                    dict.append(temp)
            return render(request, "loginsuc.html", {"name": names,"dic":dict,"t":datetime.date.today()})
        elif 'back' in request.POST:
            return render(request, "index.html")
        elif 'day' in request.POST:
            day = request.POST.get("days", None)
            names = request.POST.get("day", None)
            dict = []
            datafor4 = models.Infss.objects.all()
            for i in range(len(datafor4)):
                tempdate=datafor4[i].timenows.strftime('%Y-%m-%d')
                if (datafor4[i].trans == str(names) and str(tempdate) == str(day)):
                    temp = {'time': datafor4[i].timenows, 'id': str(datafor4[i].id), 'ids': datafor4[i].ids,
                            'score': datafor4[i].score}

                    dict.append(temp)
            return render(request, "loginsuc.html", {"name": names, "dic": dict,"t":datetime.date.today()})
        elif 'change'in request.POST:
            names = request.POST.get("change", None)
            return render(request, "change.html", {"name": names})
        else:
            names = request.POST.get("hid", None)
            t = request.POST.get("t", None)
            models.Infss.objects.get(id=int(t)).delete()
            dict = []
            datafor1 = models.Infss.objects.all()
            for i in range(len(datafor1)):
                if (datafor1[i].trans == str(names)):
                    temp = {'time': datafor1[i].timenows, 'id': str(datafor1[i].id), 'ids': datafor1[i].ids,
                            'score': datafor1[i].score}
                    dict.append(temp)
            return render(request, "loginsuc.html",{"name": names,"dic":dict,"t":datetime.date.today()})

        return render(request, "loginsuc.html", {"name": names,"t":datetime.date.today()})
    #{"name": names}
def change(request):
    if request.method == "POST":
        names = request.POST.get("t", None)
        pas1=request.POST.get("password1", None)
        pas2 = request.POST.get("password2", None)
        ori = request.POST.get("origin", None)
        if pas1==pas2:
            datafor3 = models.User.objects.get(username=names)
            if datafor3.password==ori:
                datafor3.password=pas1
                datafor3.save()
                datafor1 = models.Infss.objects.all()
                dict = []
                for i in range(len(datafor1)):
                    if (datafor1[i].trans == str(names)):
                        temp = {'time': datafor1[i].timenows, 'id': str(datafor1[i].id), 'ids': datafor1[i].ids,
                                'score': datafor1[i].score}
                        dict.append(temp)
                return render(request, "loginsuc.html", {"name": names, "dic": dict,})
            else:
                return render(request, "change.html", {"name": names})

        else:
            return render(request, "change.html", {"name": names })
def catchin(n,type):
    xdays=[]
    yscore=[]
    data = models.Infss.objects.all()
    today=datetime.date.today()
    for j in range(1,n):
        delta = datetime.timedelta(days=n-j)
        to=today-delta
        xdays.append(str(to))
        score=0
        count=0
        for i in range(len(data)):
            tempdate = data[i].timenows.strftime('%Y-%m-%d')
            if (str(tempdate) == str(to) and data[i].ids==type):
                score=score+int(data[i].score)
                count=count+1
        if count==0:
            yscore.append(0)
        else:
            yscore.append(score/count)
    return xdays,yscore