from django.shortcuts import render
import os
import django
from urllib.request import urlopen
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_backend.settings")

django.setup()

from movies.models import Location, Movies, Genre, LocationDetail, Actor

import csv, requests

# Create your views here.
## Location Model DB 저장
def location():       
    # f = open('C:/Users/SSAFY/Desktop/movie_location.csv')
    f = open('C:/Users/hanul/OneDrive/바탕 화면/movie_location.csv')
    rdr = csv.reader(f)
    title = next(rdr)
    arr = []
    for line in rdr:
        state, city = line[10],line[11]
        if (state, city) not in arr:
            arr.append((state, city))
            Location.objects.create(
                state = state,
                city = city
        )
# location()

## Movie Model DB 저장
def movie():
    file = open('C:/Users/SSAFY/Desktop/movie_location.csv', "r", encoding="cp949")
    f = csv.reader(file)
    _ = next(f)
    movies = {}
    for i in f:
        if not movies.get(i[5]):
            movies[i[5]] = i[3]

    for movie in movies:
        movieId = movie[0]
        movieSeq = movie[1:]
        URL = f'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&ServiceKey=5GV7C22AD83YQ45F32S2&movieId={movieId}&movieSeq={movieSeq}'
        response = requests.get(URL).json()
        results = response.get('Data')[0].get('Result')[0]
        # db에 저장하기
        movieId = results['movieId']
        movieSeq = results['movieSeq']
        title = results['title']
        director = results['directors']['director'][0]['directorNm']
        nation = results['nation']
        plot = results['plots']['plot'][0]['plotText']
        runtime = results['runtime']
        runtime = runtime
        rating = results['rating']
        RlsDate = results['repRlsDate']
        keywords = results['keywords']
        poster = results['posters'].split('|')[0]
        # teaser 
        URL = f'https://www.kmdb.or.kr/db/kor/detail/movie/{movieId}/{movieSeq}/own/videoData'
        response = urlopen(URL)
        soup = BeautifulSoup(response, "html.parser")

        elements = soup.select('div#anchorMovieMovie > div.mImage7 > ul > li > a')
        if elements:
            target = elements[0].attrs['href']
            t = target.replace('javascript:fcnPlay(\'', '').replace('\');', '')
            base_url = 'https://www.kmdb.or.kr/trailer/play/'
            teaser_url = base_url+t
        else:
            teaser_url=''
        Movies.objects.create(
            kmdb_id = movieId,
            kmdb_seq = movieSeq,
            movie_title = title,
            director_name = director,
            nation = nation,
            plot = plot, 
            runtime = runtime,
            rating = rating,
            release_date = RlsDate,
            keywords = keywords,
            poster = poster,
            teaser = teaser_url
        )

# movie()

## Genre Model
def genre():
    arr = []
    movies = Movies.objects.all()
    for movie in movies:
        movieId, movieSeq = movie.kmdb_id, movie.kmdb_seq
        URL = f'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&ServiceKey=5GV7C22AD83YQ45F32S2&movieId={movieId}&movieSeq={movieSeq}'
        response = requests.get(URL).json()
        results = response.get('Data')[0].get('Result')[0]
        genres = results['genre']
        genres_lst = genres.split(',')
        
        for genre in genres_lst:
            if genre not in arr and genre !='':
                arr.append(genre)
                Genre.objects.create(
                    genre = genre
                )
            if genre != '':
                genre_id = Genre.objects.get(genre=genre)
                movie.genres.add(genre_id)
                movie.save()
                
# genre()


# LocationDetail
def locationDetail():
    locations = Location.objects.all()
 
    movies = Movies.objects.all()
    for movie in movies:
        # f = open('C:/Users/SSAFY/Desktop/movie_location.csv')
        f = open('C:/Users/hanul/OneDrive/바탕 화면/movie_location.csv')
        rdr = csv.reader(f)
        _ = next(rdr)

        for lst in rdr:
            if lst[3]==movie.movie_title.strip():
                state, city  = lst[10], lst[11]
                for location in locations:
                    if (location.state, location.city) == (state, city):
                        location_id = location.id

                place = lst[2]
                latitude = lst[14]
                longitude = lst[15]
                
                LocationDetail.objects.create(
                    movie_id=movie.id,
                    location_id = location_id,
                    place = place,
                    latitude = latitude,
                    longitude = longitude,
                )

            
# locationDetail()

## Actor
def actor():
    movie_name = ''
    movies = Movies.objects.all()
    actor_id_total_lst = []
    for movie in movies:

        # movie_name = movie.movie_title
        # release_date = movie.release_date # '2019-01-09' 형식으로
        # if release_date:
        #     release_date = release_date[:4] + '-' + release_date[4:6] + '-' + release_date[6:]

        # URL = f'https://api.themoviedb.org/3/search/movie?api_key=5796ca45f3451bf2d68f3949e8f4c4de&language=ko&region=KR&query={movie_name}'
        # response = requests.get(URL).json()
        # results = response.get('results')

        # for i in results:
        #     if i.get('original_language') == 'ko':
        #         if release_date: # 개봉일 존재하는 경우
        #             if i.get('release_date') == release_date:
        #                 tmdb_id = i.get('id')
        #         else:
        #             tmdb_id = i.get('id')
        tmdb_id = movie.tmdb_id
        if tmdb_id:
            # movie.tmdb_id = tmdb_id # movie model에 tmdb_movie_id 넣어주기
            # movie.save()
            URL = f'https://api.themoviedb.org/3/movie/{tmdb_id}/credits?api_key=5796ca45f3451bf2d68f3949e8f4c4de'
            response = requests.get(URL).json()
            results = response.get('cast')

            actor_id_lst = []
            base_URL = 'https://image.tmdb.org/t/p/original'
            for ppl in results:
                if ppl['known_for_department'] == 'Acting':
                    profile_path = ppl['profile_path']
                    if profile_path:
                        profile_path = base_URL + profile_path
                    else:
                        profile_path = '' #  프로필 사진 없으면

                    actor_id_lst.append([ppl['id'],ppl['name'],profile_path])

            actor_id_lst = actor_id_lst[:9]  # 배우 9명 까지
            for i in actor_id_lst:
                actor_id = i[0]
                actor_name = i[1]
                profile_path = i[2]

                if actor_id not in actor_id_total_lst: # 중복 피하게
                    actor_id_total_lst.append(actor_id)
                # db 저장해주기
                    Actor.objects.create(
                        actor_name = actor_name,
                        tmdb_actor_id = actor_id,
                        profile_path = profile_path,
                    )

# actor()

# Movie - Actor
def movie_actor():
    movies = Movies.objects.all()
    actors = Actor.objects.all()
    for movie in movies:
        tmdb_id = movie.tmdb_id
        URL = f'https://api.themoviedb.org/3/movie/{tmdb_id}/credits?api_key=5796ca45f3451bf2d68f3949e8f4c4de'
        response = requests.get(URL).json()
        cast = response.get('cast')
        actor_id_lst = []
        for ppl in cast:
            if ppl['known_for_department'] == 'Acting':
                actor_id_lst.append(ppl['id']) 
    
        for actor in actors:  
            if int(actor.tmdb_actor_id) in actor_id_lst[:9]:
                print(actor.actor_name, movie.movie_title)
                movie.actors.add(actor.id)
                movie.save()         

# movie_actor()


### movie-location
# movie()
# location()
# locationDetail()

### Genre
# genre()

### Actor
# actor()
# movie_actor()