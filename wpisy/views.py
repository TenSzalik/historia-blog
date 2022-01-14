from django.shortcuts import render
from .models import Entry, Tag, MainPicture, Review
from .filters import EntryFilter

def glowna(request):
    article = Entry.objects.all()
    new = article.order_by('created')[:1]
    history = Entry.objects.filter(tags__name="Współczesność")
    baner = MainPicture.objects.get(title="Główny")

    return render(request, 'glowna.html', {'article': article, 'new':new, 'history': history, 'baner': baner,})

def o_mnie(request):
    return render(request, 'o_mnie.html')

articleObj = None

def wpis(request, pk):
    global articleObj
    articleObj = Entry.objects.get(id=pk)
    obj = articleObj
    obj.shows += 1
    obj.save()
    tags = articleObj.tags.all()
    #można również użyć w poj..._wpis.html {% for tag in articleObj.tags.all %} i pozbyć się z views tags = articleObj.tags.all()
    reviews = articleObj.review_set.all()
    number_reviews = reviews.count()

    return render(request, 'pojedynczy_wpis.html', {'articleObj': articleObj, 'tags':tags, 'reviews': reviews, 'number_reviews': number_reviews, 'obj': obj,})

def serce(pk):
    global articleObj
    articleObj.heart_count += 1
    articleObj.save()

def prehistoria(request):
    any_tag = Tag.objects.get(name="Prehistoria")
    tags = Entry.objects.filter(tags__name="Prehistoria").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def starożytność(request):
    any_tag = Tag.objects.get(name="Starożytność")
    tags = Entry.objects.filter(tags__name="Starożytność").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def średniowiecze(request):
    any_tag = Tag.objects.get(name="Średniowiecze")
    tags = Entry.objects.filter(tags__name="Średniowiecze").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def nowożytność(request):
    any_tag = Tag.objects.get(name="Nowożytność")
    tags = Entry.objects.filter(tags__name="Nowożytność").order_by('-created')
    
    myFilter = EntryFilter(request.GET, queryset=Entry.objects.all())
    tags = myFilter.qs
    #https://pretagteam.com/question/djangofilter-how-to-make-multiple-fields-search-with-djangofilter
    #https://stackoverflow.com/questions/66052586/django-filter-multiple-fields-search-overriding-other-parameters-django-filte

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'myFilter':myFilter,})

def współczesność(request):
    any_tag = Tag.objects.get(name="Współczesność")
    tags = Entry.objects.filter(tags__name="Współczesność").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def mikrohistoria(request):
    any_tag = Tag.objects.get(name="Mikrohistoria")
    tags = Entry.objects.filter(tags__name="Mikrohistoria").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def biografistyka(request):
    any_tag = Tag.objects.get(name="Biografistyka")
    tags = Entry.objects.filter(tags__name="Biografistyka").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def drobnenewsy(request):
    any_tag = Tag.objects.get(name="Drobne Newsy")
    tags = Entry.objects.filter(tags__name="Drobne Newsy").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def raczeknieboraczek(request):
    any_tag = Tag.objects.get(name="Raczek Nieboraczek")
    tags = Entry.objects.filter(tags__name="Raczek Nieboraczek").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def filozofia(request):
    any_tag = Tag.objects.get(name="Filozofia")
    tags = Entry.objects.filter(tags__name="Filozofia").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def literatura(request):
    any_tag = Tag.objects.get(name="Literatura")
    tags = Entry.objects.filter(tags__name="Literatura").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def refleksje(request):
    any_tag = Tag.objects.get(name="Refleksje")
    tags = Entry.objects.filter(tags__name="Refleksje").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def psychologia(request):
    any_tag = Tag.objects.get(name="Psychologia")
    tags = Entry.objects.filter(tags__name="Psychologia").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def polska(request):
    any_tag = Tag.objects.get(name="Polski Kosmos")
    tags = Entry.objects.filter(tags__name="Polski Kosmos").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})

def wynalazkiodkryciadzieła(request):
    any_tag = Tag.objects.get(name="Człowiecze Dzieło")
    tags = Entry.objects.filter(tags__name="Człowiecze Dzieło").order_by('-created')
    number_reviews = Review.objects.filter(single_entry__in=tags)

    return render(request, 'kategorie.html', {'any_tag': any_tag, 'tags': tags, 'number_reviews': number_reviews,})