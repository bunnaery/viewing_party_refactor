import pytest
from viewing_party.movie import Movie


def test_created_movie():
    # Arrange/Act
    movie_1 = Movie("Moana", "Dramedy", 4.5)

    # Assert
    assert movie_1.movie == "Moana"
    assert movie_1.genre == "Dramedy"
    assert movie_1.rating == 4.5

