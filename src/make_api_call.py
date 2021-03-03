import requests


class Api:

    def make_call_to_server(self, movie_name):
        url = "https://imdb8.p.rapidapi.com/auto-complete"

        querystring = {"q": movie_name}

        headers = {
            'x-rapidapi-key': "b9574dda6dmsh15fd109cf94156ap13974cjsnc7495f8f3eab",
            'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
