import requests, json

def get_data( difficulty : str ):
    res = requests.get(f'https://opentdb.com/api.php?amount=25&type=boolean&difficulty={ difficulty }')
    data = json.loads( res.text )
    return data['results']
