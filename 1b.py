#Questão 1 letra b
#aaa(b | c)* | (b | c)* aaa
from questao1 import StateType, State, Automata

q0 = State("q0", StateType.inicial, {"q1": "a", "q5": "bc"})
q1 = State("q1", StateType.middle, {"q2": "a"})
q2 = State("q2", StateType.middle, {"q3": "a"})
q3 = State("q3", StateType.final, {"q4": "bc"})
q4 = State("q4", StateType.final, {"q4": "bc"})
q5 = State("q5", StateType.middle, {"q5": "bc", "q6": "a"})
q6 = State("q6", StateType.middle, {"q7": "a"})
q7 = State("q7", StateType.middle, {"q8": "a"})
q8 = State("q8", StateType.final)

all_states = {"q0": q0, "q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5, "q6": q6, "q7": q7, "q8": q8}

string = "bcbcbcbcbcaa"
automata = Automata(all_states)
teste = automata.make_transition(q0, string)
print(teste)
