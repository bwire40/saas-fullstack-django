from django.shortcuts import render
# from django.http import HttpResponse

from visits.models import PageVisit
# homepage view
def home_page_view(request, *args, **kwargs):

    queryset=PageVisit.objects.all()
    pagequeryset=PageVisit.objects.filter(path=request.path)


    my_title="My page"
    my_context={
        "page_title":my_title,
        "queryset":queryset,
        "page_visit_count":pagequeryset.count(),
        "total_visit_count":queryset.count()
    }
    hmtl_template="home.html"


    path=request.path #get the path
    PageVisit.objects.create(path=request.path) #store to the db


    return render(request,hmtl_template,my_context)
    # return HttpResponse(html_)