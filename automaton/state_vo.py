class State:

    def __init__(
        self,
        name: str,
        is_final: bool,
        is_initial: bool = False,
    ) -> None:
        self.name = name
        self.is_final = is_final
        self.is_initial = is_initial

    def __str__(self) -> str:
        return f"{self.name} (Is final: {self.is_final}, Is initial: {self.is_initial})"

    def __repr__(self) -> str:
        return f"{self.name} (Is final: {self.is_final}, Is initial: {self.is_initial})"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, State):
            return False
        return self.name == value.name
