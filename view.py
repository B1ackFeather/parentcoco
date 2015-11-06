from django import HttpResponse

def hello(request):
	return HttpResponse("Hello world ! ")
