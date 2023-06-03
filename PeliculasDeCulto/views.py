from datetime import date
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import PeliculasDeCulto,Category
# Her bir metot view olarak adlandırılır

db = {
    "movies": [
        {
            "title":"El Topo",
            "description":"By Alejandro Jodorowsky. This film incorporates elements of traditional Western movies but stands out with its fantasy and psychedelic elements. It is also a dramatic and suspenseful story.",
            "imageUrl":"ElTopo.jpg",
            "slug":"El-Tapo-movie-link",
            "date": date(1970,11,18),
            "isActive":True,
            "isUpdated":True
        },
        {
            "title":"Viridiana",
            "description":"By Luis Buñuel. This film is filled with Luis Buñuel's signature absurd and black comedy elements. It can be described as a drama that questions social issues and moral values.",
            "imageUrl":"Viridiana.jpg",
            "slug":"Viridiana-movie-link",
            "date": date(1961,10,10),
            "isActive":True,
            "isUpdated":True
            
        },
         {
            "title":"Todo sobre mi madre",
            "description":"By Pedro Almodóvar. This film, with Pedro Almodóvar's distinctive style of colorful and emotional storytelling, combines elements of drama and comedy. It has a melodramatic tone and explores themes such as gender roles, motherhood, and friendship.",
            "imageUrl":"TodoSobreMiMadre.jpg",
            "slug":"Todo-sobre-mi-madre-movie-link",
            "date": date(1999,5,26),
            "isActive":True,
            "isUpdated":True
        }
    ],
    "categories": [
        {"id":1,"name":"Psychedelic","slug":"Psychedelic"},
        {"id":2,"name":"Absurd","slug":"Absurd"},
        {"id":3,"name":"Melodrama.","slug":"Melodrama"},
        ]
}

def index(request):
    #list comphension
    movies = PeliculasDeCulto.objects.all()
    categories = Category.objects.all()
    
    return render(request, 'PeliculasDeCulto/index.html', {
                  'categories': categories,
                  "movies": movies
                  })

def dizilerdetay(request, slug):
    movie = get_object_or_404(PeliculasDeCulto, slug= slug)
    context = {
        'movie': movie
    }
    return render(request, 'PeliculasDeCulto/details.html', context)

def commends(request):
    return HttpResponse('Yorumlar(commends())')

#def starsmovie(request):
#    return HttpResponse('Yıldız filmler')

def getMoviesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'PeliculasDeCulto/movies.html', {
            'category': category_name,
            'category_text':category_text
        })
    except:
        return  HttpResponseNotFound("Wrong stuff")
         
def getMoviesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("Yanlış liste")
    category_name = category_list[category_id-1]

    redirect_url = reverse('movies_by_category', args = [category_name])
    return HttpResponseRedirect(redirect_url)