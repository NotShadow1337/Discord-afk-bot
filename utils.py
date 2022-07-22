#libraries
import json

#configuration
with open('config.json') as f:
    config = json.load(f)
    token = config['token']
    guild_id = config['guild_id']
    success_emoji = config['emojis']['success']
    error_emoji = config['emojis']['failure']

#afk functions
#adds a user to the afk list
def add_afk(user_id, message):
    with open('database.json', 'r') as f:
        database = json.load(f)
    #first add userid to database then add message
    database['afks'][str(user_id)] = message
    with open('database.json', 'w') as f:
        json.dump(database, f, indent = 4)

#removes a user from the afk list
def remove_afk(user_id):
    with open('database.json', 'r') as f:
        database = json.load(f)
    #remove userid from database
    del database['afks'][str(user_id)]
    with open('database.json', 'w') as f:
        json.dump(database, f, indent = 4)

#checks if a user is afk
def is_afk(user_id):
    with open('database.json', 'r') as f:
        database = json.load(f)
    #check if userid is in database
    if user_id in database['afks']:
        return True
    else:
        return False

#gets the message of a user
def get_message(user_id):
    with open('database.json', 'r') as f:
        database = json.load(f)
    #get message of userid
    return database['afks'][str(user_id)]