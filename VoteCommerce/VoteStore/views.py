from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Contestant

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'VoteStore/category_list.html', {'categories': categories})

def contestant_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    contestants = category.contestants.all()
    return render(request, 'VoteStore/contestant_list.html', {'category': category, 'contestants': contestants})

def vote(request, contestant_id):
    contestant = get_object_or_404(Contestant, pk=contestant_id)
    if request.method == 'POST':
        contestant.votes += 1
        contestant.save()
        return redirect('contestant_list', category_id=contestant.category.id)
    return render(request, 'VoteStore/vote.html', {'contestant': contestant})
