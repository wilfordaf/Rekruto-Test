from django.shortcuts import render


def get_message(request):
    name = request.GET.get('name', 'User')
    message = request.GET.get('message', 'Hello world!')
    context = {'name': name, 'message': message}
    return render(request, 'index.html', context)
