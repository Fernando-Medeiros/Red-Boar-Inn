from app.extensions.configuration import mongo, mongo_update


def list_updates() -> list | dict:

    updates_notes = list(mongo_update.db.UPDATES.find({}))

    return updates_notes


def qnt_users() -> int:

    qnt = mongo.db.get_collection('USERS').count_documents({})

    return qnt


def online_players() -> int:
    
    qnt = list(mongo.db.USERS.find({"online":True})).__len__()

    return qnt


def show_rank():
    
    characters = list(mongo.db.USERS.find({}))

    top10 = [x['character'] for x in characters] 

    return top10[:10]

  
