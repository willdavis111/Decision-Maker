from somelists import movie_array
import random

print(f"""
1. Make a yes or no decision.
2. Food by region.
3. Movie to watch
4. Add or remove a film to the movie list""")
problem = input('Number of above problem to solve: ')

if problem == "1":
      choice_num = random.randint(0,100)
      if choice_num >= 50:
            print("Yeah it's looking like a yes to me... the computer")
      else:
            print("I'm saying no... however i am just a computer")

elif problem == "2":
      choice_num = random.randint(0, 9)
      regionsarray = ["Merican", "Mexican", "Thai", "Greek", "Indian", "Japanese", "Spanish", "French", "Chinese", "Italian"]
      region_choice = regionsarray[choice_num]
      print(f"I think it would be best to eat {region_choice} food")

elif problem == "3":
      movie_choice = random.choice(movie_array)
      movieAndGenre = movie_choice.split(':')
      movie = movieAndGenre[0]
      genre = movieAndGenre[1]
      vibe = {'d': "Emotional joy ride", 'c': "awesome piece of classic film", 'a': "action packed romp", 'j': "adventurous journey", 'f': "opportunity to giggle", 'l': "extra silly trip"}

      print(f'I think we should watch{movie} tonight!')
      print(f"Sounds Like an {vibe[genre]} to me")

elif problem == "4":
      add_remove = input("Add or Remove: ")
      film = input("fill to add: ")
      if add_remove.lower == "add":
            movie_array.append(film)
      elif add_remove.lower == "remove":
            movie_array.remove(film)
      print("Thank you!")


else:
      print("Sorry, I can't help you")


