from django.shortcuts import render
# Create your views here.
def blog(request):
    print('Página do blog')
    return render(
        request,
        'blog/index.html',
    )

def exemplo(request):
    print('Página do exemplo')
    return render(
        request,
        'blog/exemplo.html',
    )