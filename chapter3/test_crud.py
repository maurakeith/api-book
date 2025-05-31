"""Testing SQLAlchemy helper functions"""

import pytest
from datetime import date

import crud
from database import SessionLocal

# Use a test date of 4/1/2024 to test the min_last_changed_date
test_date = date(2024, 4, 1)

@pytest.fixture(scope="function")
def db_session():
    """This starts a database session and closes it when done"""
    session = SessionLocal()
    yield session
    session.close()

def test_get_player(db_session):
    """Tests getting the first player"""
    player = crud.get_player(db_session, player_id = 1001)
    assert player.player_id == 1001

def test_get_players(db_session):
    """Tests that the count of players in the database is as expected"""
    players = crud.get_players(db_session, limit=10000)
    assert len(players) == 1018

def test_get_players_by_name(db_session):
    """Tests that the count of players in the database is as expected when filtered by name"""
    players = crud.get_players(db_session, first_name="Bryce", last_name="Young")
    assert len(players) == 1
    assert players[0].player_id == 2009

def test_get_all_performances(db_session):
    """Tests that the count of performances in the database is as expected"""
    performances = crud.get_performances(db_session, limit=18000)
    assert len(performances) == 17306

def test_get_new_performances(db_session):
    """Tests that the count of performances in the database is as expected when filtered by date"""
    performances = crud.get_performances(db_session, limit=18000, min_last_changed_date=test_date)
    assert len(performances) == 2711

def test_get_player_count(db_session):
    """Tests that the player count function works as expected"""
    player_count = crud.get_player_count(db_session)
    assert player_count == 1018