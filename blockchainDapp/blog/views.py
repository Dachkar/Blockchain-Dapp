from django.shortcuts import render

posts = [
    {
        'author': 'Douglas',
        'title': 'Post 1',
        'content': 'Content of first post',
        'date_posted': 'February 16'
    },
    {
        'author': 'Mr. Miagy',
        'title': 'Post 2',
        'content': 'Content of second post',
        'date_posted': 'February 17'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Entries'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', )

