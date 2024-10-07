from .state_vo import State
from .transition_vo import Transition


class Transdutor:
    initial_state: State | None = None
    final_states: list[State] = []
    current_state: State | None = None
    states: dict[State, dict[str, Transition]] = {}

    # def __init__(
    #     self,
    #     initial_state: State,
    #     final_states: list[State],
    #     current_state: State,
    #     states: dict[State, dict[str, Transition]],
    # ) -> None:
    #     self.initial_state = initial_state
    #     self.final_states = final_states
    #     self.current_state = current_state
    #     self.states = states

    def add_state(self, state: State) -> None:
        if self.already_have_initial_state() and state.is_initial:
            raise Exception("Automaton already have an initial state")
        if state.is_initial:
            self.initial_state = state
        if state.is_final:
            self.final_states.append(state)
        if state in self.states:
            pass
        self.states[state] = {}

    def add_states(self, states: list[State]) -> None:
        [self.add_state(state) for state in states]

    def add_transition(self, transition: Transition) -> None:
        if transition.start not in self.states:
            raise Exception("Start state not in states")
        if transition.end not in self.states:
            raise Exception("End state not in states")
        if transition.value in self.states[transition.start]:
            raise Exception("Transition for that value already exist")

        self.states[transition.start][transition.value] = transition

    def add_transitions(self, transitions: list[Transition]) -> None:
        [self.add_transition(transition) for transition in transitions]

    def already_have_initial_state(self) -> bool:
        return self.initial_state is not None

    def make_transition(self, state: State, value: str = "") -> str:
        if state not in self.states:
            raise Exception(f"State {state} not in states")
        if value not in self.states[state]:
            raise Exception(f"Transition value '{value}' not in state {state}")
        transition = self.states[state][value]
        self.current_state = transition.end
        return transition.output

    def stop(self) -> None:
        if not (self.current_state and self.current_state.is_final):
            raise Exception("Automaton is not in a final state")
        self.current_state = None

    def reset(self) -> None:
        self.current_state = self.initial_state

    def run(self, chain: str):
        self.reset()
        for char in chain:
            if self.current_state is None:
                raise Exception("Automaton is not in a state")
            self.make_transition(self.current_state, char)
        self.stop()
