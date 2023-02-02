## Game State
game = {"tool": 0, "money": 0}

tools = {
{"name" : "Small Net", "profit": 10, "cost": 0},
{"name" : "Big Net", "profit": 100, "cost": 100}
}

## Game Option Function

def clean_pool():
    tool = tools[game["tool"]]
    print(f"You clean a pool with your {tool['name']} and make {tool['profit']}")
    game["money"] += tool["profit"]
    
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have {game['money']} and are using a {tool['name']}")
    
def upgrade():
    next_tool = tools[game["tool"]+1]
    if(next_tool == None):
        print("There are no more tools")
        return 0
    
    if(game["money"] < next_tool["cost"]):
        print("Not enough to buy tool")
        return 0
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    
def win_check():
    if(game["tool"] == 1 and game["money"] == 1000):
        print("You win")
        return True
    return False