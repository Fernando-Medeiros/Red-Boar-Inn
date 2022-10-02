from flask import current_app as app


def list_updates() -> list | dict:

    return list(app.db_update.UPDATES.find({}))[:14].__reversed__()


def qnt_users() -> int:
    
    return app.db.get_collection('USERS').count_documents({})


def online_players() -> int:
  
    return list(app.db.USERS.find({"online":True})).__len__()
    


def show_rank() -> list | dict:
    
    characters: list = list(app.db.USERS.find({}))

    top10: dict = [x['character'] for x in characters] 

    return top10[:10]

  
