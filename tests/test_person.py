import pytest
from viewing_party.person import Person
from viewing_party.movie import Movie


def test_create_person():
    # Arrange / Act
    kendall = Person("Kendall", ["Nancy"])

    # Assert
    assert isinstance(kendall, Person)

def test_person_name_is_set_correctly():
    # Arrange / Act
    nancy = Person("Nancy", ["Kendall"])
    danica = Person("Danica", ["Ping"])

    # Assert
    assert nancy.name == "Nancy"
    assert danica.name == "Danica"

def test_person_friends_list_is_set_correctly():
    # Arrange / Act
    ana = Person("Ana", ["Ariel"])

    # Assert
    assert ana.friends == ["Ariel"]

def test_friend_added_to_person():
    # Arrange
    laura = Person("Laura", ["Sage"])

    # Act
    laura.add_friend("Elizabeth")

    # Assert
    assert laura.friends == ["Sage", "Elizabeth"]

def test_no_duplicate_friends_added():
    # Arrange
    moyo = Person("Moyo", ["Sarah"])

    # Act
    moyo.add_friend("Sarah")

    # Assert
    assert moyo.friends == ["Sarah"]

def test_add_movie_to_watchlist():
    # Arrange
    super_mario_bros = Movie("Super Mario Bros", "Comedy", 0)
    jasmine = Person("Jasmine", "Mikayla")

    # Act
    jasmine.add_movie(super_mario_bros)

    # Assert
    assert jasmine.watchlist == [super_mario_bros]

def test_removed_movie_from_watchlist_and_add_to_watched(): 
    # Arrange 
    super_mario_bros = Movie("Super Mario Bros", "Comedy", 0)
    jasmine = Person("Jasmine", "Mikayla")

    # Act
    jasmine.add_movie(super_mario_bros)
    jasmine.watch_movie(super_mario_bros)

    # Assert
    assert len(jasmine.watchlist) == 0
    assert jasmine.watched == [super_mario_bros]