class PartialChannel:
    """An object with limited channel information.

    Args:
        id_ (str): The channel ID.
        name (str): The channel name.

    Attributes:
        id (str): The channel ID.
        name (str): The channel name.
    """

    __slots__ = ("id", "name")

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
