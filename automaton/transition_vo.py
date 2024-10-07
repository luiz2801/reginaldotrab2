from automaton.state_vo import State


class Transition:

    def __init__(self, start: State, end: State, value: str, output: str = "") -> None:
        self.start = start
        self.end = end
        self.value = value
        self.output = output

    def __str__(self) -> str:
        return f"{self.start} --{self.value}/{self.output}--> {self.end}"

    def __repr__(self) -> str:
        return f"{self.start} --{self.value}/{self.output}--> {self.end}"
