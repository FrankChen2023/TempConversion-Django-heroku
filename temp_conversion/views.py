from django.shortcuts import render

# Create your views here.
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 

def conversion(temp, curr):
    if curr == "F":
        converted_t = (temp-32)*0.5556
        dest = "C"
    else:
        converted_t = temp/0.5556 + 32
        curr = "C"
        dest = "F"
    return converted_t, curr, dest

def index(request):
    converted_t = None
    temp = None
    dest = None
    curr = None
    if request.method=="POST":
        curr = request.POST.get("rd",'')
        temp = int(request.POST.get('temp',''))
        converted_t, curr, dest = conversion(temp, curr)
    return render(request, "index.html", {'converted_t':converted_t, 'temp':temp, 'curr':curr, 'dest':dest})


