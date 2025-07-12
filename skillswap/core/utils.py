from .models import Profile,OfferedSkill
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def paginateProfiles(request,profiles,results):
    page=request.GET.get('page')
    paginator=Paginator(profiles,results)
    try:
        profiles=paginator.page(page)
    except PageNotAnInteger:
        page=1
        profiles=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        profiles=paginator.page(page)
    leftpage=int(page)-4
    if leftpage<1:
        leftpage=1
    rightpage=int(page)+5
    if rightpage>paginator.num_pages:
        rightpage=paginator.num_pages
    custom_range=range(leftpage,rightpage+1)
    return custom_range,profiles


def searchProfiles(request):
    search_query=""
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    skills=OfferedSkill.objects.filter(name__icontains=search_query)
    profiles=Profile.objects.distinct().filter(profile='public')
    profiles=profiles.filter(Q(name__icontains=search_query) | 
                                               Q(name__in=skills))
    return profiles,search_query