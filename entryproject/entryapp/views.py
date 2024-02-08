from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('<h2>hello world from entryapp</h2>')