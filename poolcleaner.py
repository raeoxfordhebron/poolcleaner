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