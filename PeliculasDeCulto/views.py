from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# Her bir metot view olarak adlandırılır

db = {
    "movies": [
        {
            "title":"El Topo",
            "description":"By Alejandro Jodorowsky. This film incorporates elements of traditional Western movies but stands out with its fantasy and psychedelic elements. It is also a dramatic and suspenseful story.",
            "imageUrl":"https://m.media-amazon.com/images/M/MV5BNmUzMWQzMTItYzZiOS00NmI1LWIzMTgtOWE4NzE1M2NhY2IxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
            "slug":"El-Tapo-movie-link",
            "date": date(1970,11,18),
            "isActive":True,
            "isUpdated":True
        },
        {
            "title":"Viridiana",
            "description":"By Luis Buñuel. This film is filled with Luis Buñuel's signature absurd and black comedy elements. It can be described as a drama that questions social issues and moral values.",
            "imageUrl":"https://m.media-amazon.com/images/M/MV5BZTk4ODhmNDEtM2RlMS00ZWEyLWJlY2YtODcyZGRlMDEwOGI5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
            "slug":"Viridiana-movie-link",
            "date": date(1961,10,10),
            "isActive":True,
            "isUpdated":True
            
        },
         {
            "title":"Todo sobre mi madre",
            "description":"By Pedro Almodóvar. This film, with Pedro Almodóvar's distinctive style of colorful and emotional storytelling, combines elements of drama and comedy. It has a melodramatic tone and explores themes such as gender roles, motherhood, and friendship.",
            "imageUrl":"https://m.media-amazon.com/images/M/MV5BODMyYTc3YmItZDYwZC00ZmU1LTgyNGUtMDU4NDhiOWExNmU3XkEyXkFqcGdeQXVyMTI3ODAyMzE2._V1_.jpg",
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
    movies = [movie for movie in db["movies"] if movie["isActive"] == True]
    categories = db["categories"]
    
    return render(request, 'PeliculasDeCulto/index.html', {
                  'categories': categories,
                  "movies": movies
                  })

def dizilerdetay(request, movie_name):
    return HttpResponse(f'{movie_name} Dizi Detaylari(dizilerdetay())')

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