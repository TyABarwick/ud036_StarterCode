import media
import fresh_tomatoes

"""This module instantiates movie objects and calls the open_movies_page function to render the HTML."""
    
the_day_after_tomorrow = media.Movie("The Day After Tomorrow",
                                     "https://upload.wikimedia.org/wikipedia/en/5/58/The_Day_After_Tomorrow_movie.jpg",
                                     "https://www.youtube.com/watch?v=Ku_IseK3xTc")

rock_star = media.Movie("Rock Star",
                        "https://upload.wikimedia.org/wikipedia/en/f/fa/Rock_star_ver1.jpg",
                        "http://www.youtube.com/watch?v=-OTQoNvgyYs")

the_proposal = media.Movie("The Proposal",
                           "https://upload.wikimedia.org/wikipedia/en/0/02/The_Proposal.jpg",
                           "https://www.youtube.com/watch?v=RFL8b1p1ELY")

movies=[the_day_after_tomorrow, rock_star, the_proposal]

# Function to render HTML page
fresh_tomatoes.open_movies_page(movies)

