#Questão 1 letra d
#a*b* (a | ac*)
from questao1 import StateType, State, Automata

q0 = State("q0", StateType.inicial, {"q1": "a", "q2": "b"})
q1 = State("q1", StateType.final, {"q1": "a", "q2": "b", "q4": "c"})
q2 = State("q2", StateType.middle, {"q3": "a", "q2": "b"})
q3 = State("q3", StateType.final, {"q4": "c"})
q4 = State("q4", StateType.final, {"q4": "c"})

all_states = {"q0": q0, "q1": q1, "q2": q2, "q3": q3, "q4": q4}

string = "bbbbbbbbbba"
automata = Automata(all_states)
teste = automata.make_transition(q0, string)
print(teste)
