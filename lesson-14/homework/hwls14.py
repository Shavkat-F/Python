import json
import requests
import random

# Task 1: JSON Parsing
def parse_students(filename='students.json'):
    try:
        with open(filename, 'r') as f:
            students = json.load(f)
            for student in students:
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    except Exception as e:
        print(f"Error reading students.json: {e}")

# Task 2: Weather API
def get_weather(city="Tashkent", api_key="your_api_key_here"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f"Weather in {city}: {description}, Temperature: {temp}°C, Humidity: {humidity}%")
    else:
        print("Failed to fetch weather data.")

# Task 3: JSON Modification
def load_books(filename='books.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books, filename='books.json'):
    with open(filename, 'w') as f:
        json.dump(books, f, indent=4)

def add_book(title, author, year):
    books = load_books()
    books.append({'title': title, 'author': author, 'year': year})
    save_books(books)
    print("Book added.")

def update_book(title, new_info):
    books = load_books()
    for book in books:
        if book['title'] == title:
            book.update(new_info)
            save_books(books)
            print("Book updated.")
            return
    print("Book not found.")

def delete_book(title):
    books = load_books()
    new_books = [book for book in books if book['title'] != title]
    if len(new_books) < len(books):
        save_books(new_books)
        print("Book deleted.")
    else:
        print("Book not found.")

# Task 4: Movie Recommendation System
def recommend_movie_by_genre(genre, api_key="your_api_key_here"):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'Search' in data:
            movie = random.choice(data['Search'])
            print(f"Recommended Movie: {movie['Title']} ({movie['Year']})")
        else:
            print("No movies found for this genre.")
    else:
        print("Failed to fetch movie data.")
