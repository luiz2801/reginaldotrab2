import re
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
            return "ACCEPTED"
        
        if characters:
            char = characters[0]
            if current_state.transitions == None:
                return "NOT ACCEPTED"
            for state in current_state.transitions:
                if char in current_state.transitions[state]:
                    next_state = self.states[state]
                    characters = characters[1:]
                    
                    result = self.make_transition(next_state, characters)
                    if result == "ACCEPTED":
                        return "ACCEPTED"
        
        return "NOT ACCEPTED" 


q1 = State("q1", StateType.inicial, {"q2": "c"})
q2 = State("q2", StateType.middle, {"q3": "o"})
q3 = State("q3", StateType.middle, {"q4": "m"})
q4 = State("q4", StateType.middle, {"q5": "p"})
q5 = State("q5", StateType.middle, {"q6": "u"})
q6 = State("q6", StateType.middle, {"q7": "t"})
q7 = State("q7", StateType.middle, {"q8": "a"})
q8 = State("q8", StateType.middle, {"q9": "d"})
q9 = State("q9", StateType.middle, {"q10": "o"})
q10 = State("q10", StateType.middle, {"q11": "r"})
q11 = State("q11", StateType.final)

all_states = {
    "q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5, "q6": q6, "q7": q7, "q8": q8, "q9": q9, "q10": q10, "q11": q11
    }

text = """O computador é uma máquina capaz de variados tipos de tratamento automático de
informações ou processamento de dados. Entende-se por computador um sistema físico que
realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são
ícones da era da informação. O primeiro computador eletromecânico foi construído por
Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador 
pessoal ou ainda computador doméstico"""

all_strings = re.split(r"(\s)", text)

automata = Automata(all_states)
position = 0

all_strings = re.split(r"(\s)", text)

for current_string in all_strings:
    teste = automata.make_transition(q1, current_string)
    position += len(current_string)
    if teste == "ACCEPTED":
        print(current_string)
        print(f"Início: {position - len(current_string)}, Fim: {position}")