from django.shortcuts import render, redirect
from .models import Post, Transactions
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from users.models import Profile


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Entries'
    }
    return render(request, 'blog/home.html', context)


def itemsold(request, pk):
    if request.method == 'POST':
        user = request.user
        storeEntry = Post.objects.all().filter(id=pk).first()
        userProfile = Profile.objects.all().filter(user=user).first()
        authorProfile = Profile.objects.all().filter(user=storeEntry.author).first()
        if userProfile.money > storeEntry.price:
            newbalance = userProfile.money - storeEntry.price
            userProfile.money = newbalance
            authorProfile.money = authorProfile.money + storeEntry.price
            userProfile.save()
            authorProfile.save()
            Transactions.objects.create(item=storeEntry.name, buyer=user)
            Post.objects.all().filter(id=pk).delete()
            messages.success(request, f'Success! You just bought {storeEntry}. Your balance is now {userProfile.money}')
            return redirect(reverse('blog-home'))
        else:
            messages.warning(request, f'{user}, you don\'t have enough money to buy {storeEntry}!')
            return redirect(reverse('blog-home'))
def transactions(request):
    context = {
        'posts': Transactions.objects.all(),
        'title': 'Entries'
    }
    return render(request, 'blog/transactions.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['name', 'description', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['name', 'description', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html', )

