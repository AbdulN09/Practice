from django.http import HttpResponse

def practice(request):
    return HttpResponse("welcome to the world")


def demo1(request):
    return HttpResponse("how are you")
