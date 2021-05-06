from django.shortcuts import render
import datetime
# Create your views here.
def a1(request):
    return render(request,'html/home.html')
def movie(request):
    news1='abc edjawdjiowj jefiejoif'
    news2='nckwiowqijwv kejfi jrflolkjfo'
    news3='nlklksejlf b.kofpoej lkjlfj'
    my_dict={'news1':news1,'news2':news2,'news3':news3}
    return render(request,'html/mnews.html',my_dict)
def sport(request):
    sport1='vldoi kwokokropfsff '
    sport2='lrkjel jj ljwolerj owl'
    sport3='nsflksejflke'
    my_dict1={'sport1':sport1,'sport2':sport2,'sport3':sport3}
    return render(request,'html/snews.html',my_dict1)
def politics(request):
    poli1='dlakdk okowkqodp'
    poli2='fwei oekopwkpo'
    poli3='klrfjioejfi'
    my_dict2={'poli1':poli1,'poli2':poli2,'poli3':poli3}
    return render(request,'html/pnews.html',my_dict2)
