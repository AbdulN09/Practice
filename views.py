from django.http import HttpResponse

def demo(request):
    return HttpResponse("hello world")


def demo1(request):
    return HttpResponse("how are you")
