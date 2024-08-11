import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_ = "title")

listofmovies = [movies.getText() for movies in all_movies]
# print(listofmovies)

ordered_listofmovies = listofmovies[::-1]
# print(ordered_listofmovies)

with open("Top_100_Movies", mode="w") as file:
    for content in ordered_listofmovies:
        file.write(f"{content}\n")