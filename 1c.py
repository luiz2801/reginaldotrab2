#Questão 1 letra c
#a*b | ab*
from questao1 import StateType, State, Automata

q0 = State("q0", StateType.inicial, {"q4": "a", "q1": "b"})
q1 = State("q1", StateType.final)
q2 = State("q2", StateType.middle, {"q2": "a", "q1": "b"})
q3 = State("q3", StateType.final, {"q3": "b"})
q4 = State("q4", StateType.final, {"q2": "a", "q5": "b"})
q5 = State("q5", StateType.final, {"q3": "b"})

all_states = {"q0": q0, "q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5}

string = "aab"
automata = Automata(all_states)
teste = automata.make_transition(q0, string)
print(teste)
