import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
  "A story of a boy and his toys that come to life",
  "https_//upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
  "https://www.youtube.com/watch?v=vwyZH85NQC4")
  
#print(toy_story.storyline) 

avatar = media.Movie("Avatar",
  "A marine on an alien planet",
  "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
  "http://www.youtube.com/watch?v=~9ceBgWV8io")
#print(avatar.storyline) 
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
  "Using rock music to learn",
  "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
  "http://www.youtube.com/watch?v=3PsUJFEBC74")
  
ratatouille = media.Movie("Ratatouille",
  "A rat is a chef in Paris",
  "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
  "http://www.youtube.com/watch?v=c3sBBRxDAqk")
  
midnight_in_paris = media.Movie("Midnight in Paris",
  "Going back in time to meet authors",
  "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
  "http://www.youtube.com/watch?v=atLg2wQQxvU")
  
hunger_games = media.Movie("Hunger Games",
  "A really  real reality show",
  "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
  "https://www.youtube.com/watch?v=PbA63a7H0bo")
   
   
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]   
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print("Dict: "+str(media.Movie.__dict__))
print("Name: "+str(media.Movie.__name__))
print("Baeses: "+str(media.Movie.__bases__))
print("Doc: "+str(media.Movie.__doc__))
print("Module: "+str(media.Movie.__module__))
print("__print whole toy_stoy object as a string__")
print(str(toy_story))
