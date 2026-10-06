from django.shortcuts import render, redirect,get_object_or_404
from .models import Genre
from .forms import CreateGenreForm, UpdateGenreForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def display_genre(request):
    all_genre = Genre.objects.all()#.order_by("-id")
    # paginate = Paginator(object_list, number of rows of your table)
    paginate = Paginator(all_genre, 10)
    page_number = request.GET.get("page")
    page_obj = paginate.get_page(page_number)
    if request.method == "POST":
        create_genre_form = CreateGenreForm(request.POST)
        if create_genre_form.is_valid():
            create_genre_form.save()
            return redirect("genres:display_genre")

    else:
        create_genre_form = CreateGenreForm()

    franco = {
        "display_genres":page_obj,
        "genre_form":create_genre_form
    }
    return render(request,"Genre/display_genre.html",franco)


@login_required
def delete_genre(request,pk):
    get_genre = Genre.objects.get(id=pk)
    get_genre.delete()
    return redirect("genres:display_genre")

@login_required
def update_genre(request,genre_pk):
    get_genre = get_object_or_404(Genre,id=genre_pk)
    if request.method == "POST":
        update_genre_form = UpdateGenreForm(request.POST,instance=get_genre)
        if update_genre_form.is_valid():
            update_genre_form.save()
            return redirect("genres:display_genre")
    else:
        update_genre_form = UpdateGenreForm(instance=get_genre)

    context = {
        "update_genre_form":update_genre_form
    }
    return render(request,"Genre/update_genre.html",context)