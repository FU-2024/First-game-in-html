def start_game():
    # Initialize game state
    game_state = {
        'score': 0,
        'level': 1,
        'is_running': True
    }
    return game_state

def update_game_state(game_state, action):
    # Update game state based on player action
    if action == 'score':
        game_state['score'] += 1
    elif action == 'diamond':
        game_state['score'] += 150
    elif action == 'level_up':
        game_state['level'] += 1
    elif action == 'end':
        game_state['is_running'] = False
    return game_state

def get_game_status(game_state):
    # Return current game status
    return {
        'score': game_state['score'],
        'level': game_state['level'],
        'is_running': game_state['is_running']
    }