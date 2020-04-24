from django.shortcuts import render

# Create your views here.
def showmovies(request):
    return render(request,"movie.html")



 # def movielist(request):
 #    no = request.GET.get("mno")
 #    print(no)
 #    if no == '1':
 #        data = {"link": }
 #    elif no == '2':
 #        data = {"link": }
 #    else:
 #        data = {"link": }
 #
 #    return render(request, "trailer.html", data)
 #
def tollywood(request):
    return render(request,"tollywood.html")

def playtollywood(request):
    no = request.GET.get("mno")
    print(no)
    if no == '1':
        data = {"link": 'https://www.youtube.com/embed/Vioy202FuaM'}
    elif no == '2':
        data = {"link": 'https://www.youtube.com/embed/5xwRV6os5Ew'}
    else:
        data = {"link": 'https://www.youtube.com/embed/4rnNzBZMqkQ'}

    return render(request, "trailer.html", data)

def bollywood(request):
    return render(request,"bollywood.html")

def playbollywood(request):
    no = request.GET.get("mno")
    print(no)
    if no == '1':
        data = {"link": 'https://www.youtube.com/embed/4f9jIdg4rTQ'}
    elif no == '2':
        data = {"link": 'https://www.youtube.com/embed/SVj26LvQMPA'}
    else:
        data = {"link": 'https://www.youtube.com/embed/fo9EhcwQXcM'}

    return render(request, "trailer.html", data)


def hollywood(request):
    return render(request,"hollywood.html")


def playhollywood(request):
    no = request.GET.get("mno")
    print(no)
    if no == '1':
        data = {"link": 'https://www.youtube.com/embed/Z1BCujX3pw8'}
    elif no == '2':
        data = {"link": 'https://www.youtube.com/embed/QGu6InUcdUY'}
    else:
        data = {"link": 'https://www.youtube.com/embed/6Q7vVt-MeXk'}

    return render(request, "trailer.html", data)


def booking(request):
    return render(request,"book.html")


def oms(request):
    return render(request,"oms.html")