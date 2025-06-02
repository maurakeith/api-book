"""SQLAlchemy query functions"""

from sqlalchemy.orm import Session, joinedload
from datetime import date

import models

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.player_id == player_id).first()

def get_players(db: Session, skip: int=0, limit: int=100, minimum_last_changed_date: date=None, last_name: str=None, first_name: str=None):
    query = db.query(models.Player)
    if minimum_last_changed_date:
        query = query.filter(models.Player.last_changed_date >= minimum_last_changed_date)
    if last_name:
        query = query.filter(models.Player.last_name == last_name)
    if first_name:
        query = query.filter(models.Player.first_name == first_name)
    return query.offset(skip).limit(limit).all()

def get_performances(db: Session, skip: int=0, limit: int=100, minimum_last_changed_date: date=None):
    query = db.query(models.Performance)
    if minimum_last_changed_date:
        query = query.filter(models.Performance.last_changed_date >= minimum_last_changed_date)
    return query.offset(skip).limit(limit).all()

def get_league(db :Session, league_name: str=None):
    query = db.query(models.League)
    if league_name:
        query = query.filter(models.League.league_name == league_name)
    return query.first()

def get_leagues(db :Session, skip: int=0, limit: int=100, minimum_last_changed_date: date=None, league_name: str=None):
    query = db.query(models.League).options(joinedload(models.League.teams))
    if minimum_last_changed_date:
        query = query.filter(models.League.minimum_last_changed_date >= minimum_last_changed_date)
    if league_name:
        query = query.filter(models.League.league_name == league_name)
    return query.offset(skip).limit(limit).all()

def get_teams(db: Session, skip: int=0, limit: int=100, minimum_last_changed_date: date=None, team_name: str=None, league_id: int=None):
    query = db.query(models.Team)
    if minimum_last_changed_date:
        query = query.filter(models.Team.last_changed_date >= minimum_last_changed_date)
    if team_name:
        query = query.filter(models.Team.team_name == team_name)
    if league_id:
        query = query.filter(models.Team.league_id == league_id)
    return query.offset(skip).limit(limit).all()

# Analytics queries
def get_player_count(db: Session):
    query = db.query(models.Player)
    return query.count()

def get_team_count(db: Session):
    query = db.query(models.Team)
    return query.count()

def get_league_count(db: Session):
    query = db.query(models.League)
    return query.count()


    