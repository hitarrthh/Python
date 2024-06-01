import pandas as pd

data = pd.read_csv('movies.csv')

ans = ['Action', 'Comedy', 'Drama', 'Crime', 'Adventure', 'Mystery', 'History', 'Biography',
       'Thriller', 'Romance', 'Family', 'Horror', 'Sci-Fi', 'Music', 'War', 'Western', 'Animation',
       'Film-Noir']
ans.sort()

print("Choose Genre:")
for index, genre in enumerate(ans, start=1):
    print(f"{index}. {genre}")

genre_choice = input("Enter the number of your desired genre: ")

try:
    genre_choice = int(genre_choice)
    if genre_choice < 1 or genre_choice > len(ans):
        print("Invalid choice. Please enter a number within the range.")
        exit()
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

selected_genre = ans[genre_choice - 1]

selected_adult = input("Choose 'Yes' or 'No' for Adult Content: ")

if selected_adult not in ['Yes', 'No']:
    print("Invalid choice for Adult Content.")
    exit()

recommend = data[
    (data['genre'].str.contains(selected_genre, case=False, na=False)) & (data['adult'] == selected_adult)
]

if recommend.empty:
    print("SORRY, NO MOVIES FOUND FOR YOUR CRITERIA")
else:
    print("RECOMMENDED MOVIES FOR YOU ARE:")
    recommended_movies = recommend.sort_values(by='rating', ascending=False)['title'].reset_index(drop=True)
    print(recommended_movies)

    filtered_genre_gross = recommend.groupby('genre')['gross'].sum().sort_values(ascending=False)
    print("\nGross Earnings by Genre")
    print(filtered_genre_gross)
