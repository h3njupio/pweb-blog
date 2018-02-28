from django.shortcuts import render

def misc_list(request):
    return render(request, 'misc/misc_list.html')

