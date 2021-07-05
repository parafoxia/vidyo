class PartialChannel:
    def __init__(self, id_: str, name: str) -> None:
        self.id = id_
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<PartialChannel id={self.id} name={self.name}>"

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __ne__(self, other) -> bool:
        return self.id != other.id
