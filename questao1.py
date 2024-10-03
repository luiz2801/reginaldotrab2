class StateType:
    inicial = 0
    inicial_final = 1
    middle = 2
    final = 3


class State:
    def __init__(self, name: str, state_type: StateType, transitions: dict | None = None) -> None:
        self.name = name
        self.state_type = state_type
        self.transitions = transitions



class Automata:
    def __init__(self, states: dict) -> None:
        self.states = states
    
    def make_transition(self, current_state: State, characters: str) -> State:
        if characters == "" and (current_state.state_type == StateType.final or current_state.state_type == StateType.inicial_final):
            print("Final state: ", current_state.name)
            return "ACCEPTED"
        
        if characters:
            char = characters[0]
            for state in current_state.transitions:
                if char in current_state.transitions[state]:
                    next_state = self.states[state]
                    characters = characters[1:]
                    
                    print(current_state.name)
                    
                    result = self.make_transition(next_state, characters)
                    if result == "ACCEPTED":
                        return "ACCEPTED"
        
        return "NOT ACCEPTED" 
