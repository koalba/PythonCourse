import os

logo = """
     ______  __ __    ___       ___   __ __  ____  _____ 
    |      ||  |  |  /  _]     /   \ |  |  ||    ||     |
    |      ||  |  | /  [_     |     ||  |  | |  | |__/  |
    |_|  |_||  _  ||    _]    |  Q  ||  |  | |  | |   __|
      |  |  |  |  ||   [_     |     ||  :  | |  | |  /  |
      |  |  |  |  ||     |    |     ||     | |  | |     |
      |__|  |__|__||_____|     \__,_| \__,_||____||_____|
      ____   ____  ___ ___    ___                        
     /    | /    ||   |   |  /  _]                       
    |   __||  o  || _   _ | /  [_                        
    |  |  ||     ||  \_/  ||    _]                       
    |  |_ ||  _  ||   |   ||   [_                        
    |     ||  |  ||   |   ||     |                       
    |___,_||__|__||___|___||_____| 
"""

def clear():
    os.system('clear')
    print( logo )