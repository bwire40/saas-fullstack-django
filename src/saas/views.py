from django.shortcuts import render
# from django.http import HttpResponse

# homepage view
def home_page_view(request, *args, **kwargs):
    my_title="My page"
    my_context={
        "page_title":my_title
    }
    hmtl_template="home.html"
    return render(request,hmtl_template,my_context)
    # return HttpResponse(html_)