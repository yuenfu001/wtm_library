from django.shortcuts import render, redirect
from django.http import HttpResponse
# to have to my database, Import models module
from .models import Author
from .forms import CreateAuthorEntry,UpdateAuthorEntry
# Create your views here.
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def author_view(request):
    # return HttpResponse("<h2>This is a registered Author Application</h2> <strong>Yeay our first application in Django under development </strong>")
    all_author = Author.objects.all().order_by("-id")
    paginate = Paginator(all_author, 10)
    page_number = request.GET.get("pages")
    page_obj = paginate.get_page(page_number)

    raghad = {
        "page_obj":page_obj
    }
    return render(request,"author/display_author.html",raghad) #{"display_all_author":all_author}

@login_required
def author_entry(request):
    if request.method == "POST":
        author_form = CreateAuthorEntry(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("display_authors")

    else:
        author_form = CreateAuthorEntry()

    context ={
        "create_form":author_form
    }
    return render(request,"author/create_author.html",context)

@login_required
def update_author(request,author_pk):
    get_unique_author = Author.objects.get(id=author_pk)
    # Requests
    #get, put, post : create/update/delete
    if request.method == "POST":
        update_form = UpdateAuthorEntry(request.POST, instance=get_unique_author)
        if update_form.is_valid():
            update_form.save()
            return redirect("display_authors")
    else:
        update_form = UpdateAuthorEntry(instance=get_unique_author)

    dictionary = {
        "update_author":update_form
    }
    return render(request,"author/update_author.html",dictionary)

@login_required
def delete_author(request,author_id):
    get_unique_author = Author.objects.get(id=author_id)
    get_unique_author.delete()
    return redirect("display_authors")
    
