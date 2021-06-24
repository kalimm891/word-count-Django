from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def wordcount(request):
    data = request.GET['data']
    li = data.split()
    di ={}
    for i in li:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    return render(request,'result.html',{'data':data,'total':len(li),'words':di})

