from questao1 import StateType, State, Automata
#1 questão letra a
#(ab*c*)*

string = ""
q0 = State("q0", StateType.inicial_final, {"q1": "a"})
q1 = State("q1", StateType.final, {"q1": "a", "q2": "b", "q3": "c"})
q2 = State("q2", StateType.final, {"q1": "a", "q2": "b", "q3": "c"})
q3 = State("q3", StateType.final, {"q1": "a", "q3": "c"})

all_states = {"q0": q0, "q1": q1, "q2": q2, "q3": q3}

automata = Automata(all_states)
teste = automata.make_transition(q0, string)
print(teste)