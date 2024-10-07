from automaton.automaton_entity import Transdutor
from automaton.state_vo import State
from automaton.transition_vo import Transition

transdutor = Transdutor()

# Definir os estados
q0 = State("q0", is_initial=True, is_final=True)
q1 = State("q1", is_final=True)
q2 = State("q2", is_final=True)
q3 = State("q3", is_final=True)

transdutor.add_states([q0, q1, q2, q3])

# q0
t1 = Transition(start=q0, end=q1, value="25", output="0")
t2 = Transition(start=q0, end=q2, value="50", output="0")
t3 = Transition(start=q0, end=q0, value="100", output="1")

# q1
t4 = Transition(start=q1, end=q2, value="25", output="0")
t5 = Transition(start=q1, end=q3, value="50", output="0")
t6 = Transition(start=q1, end=q1, value="100", output="1")

# q2
t7 = Transition(start=q2, end=q3, value="25", output="0")
t8 = Transition(start=q2, end=q0, value="50", output="1")
t9 = Transition(start=q2, end=q2, value="100", output="1")

# q3
t10 = Transition(start=q3, end=q0, value="25", output="1")
t11= Transition(start=q3, end=q1, value="50", output="1")
t12 = Transition(start=q3, end=q3, value="100", output="1")

transdutor.add_transitions([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12])


# Função para processar a sequência de moedas
def processar_transdutor(transdutor, sequencia_moedas):
    transdutor.reset()
    estado_atual = transdutor.current_state
    saidas = []

    for moeda in sequencia_moedas:
        moeda_str = str(moeda)
        try:
            output = transdutor.make_transition(estado_atual, moeda_str)
            saidas.append(output)
            estado_atual = transdutor.current_state
        except Exception as e:
            saidas.append("Erro")
            print(f"Erro ao processar moeda {moeda}: {e}")
            break
    return saidas

if __name__ == "__main__":
    sequencia_moedas = [50, 25, 50, 100, 25, 50, 100]
    saida_esperada = ["0", "0", "1", "1", "0", "1", "1"]

    saida_obtida = processar_transdutor(transdutor, sequencia_moedas)

    # Imprimir os resultados
    print("Entrada: ", sequencia_moedas)
    print("Saída esperada: ", saida_esperada)
    print("Saída obtida:    ", saida_obtida)


