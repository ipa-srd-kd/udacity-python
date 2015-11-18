import webbrowser

class Movie() :
  """ This class provides a way to store movie related information """

  VALID_RATINGS = ["G","PG","PG-13","R"]
  
  def __init__(self, movie_title, movie_storyline, movie_poster_image,movie_trailer_youtube):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = movie_poster_image
    self.trailer_youtube_url = movie_trailer_youtube
    
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
    
  def __str__(self):
    return ("Title: "+ str(self.title) + "\n" + "Storyline: " + str(self.storyline) + "\n" + "Poster: " + str(self.poster_image_url) + "\n"+ "Trailer" + str(self.trailer_youtube_url) + "\n")
