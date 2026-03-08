from app.strategies.display import display_strategies
from app.strategies.print import print_strategies
from app.strategies.serialize import serializers


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        strategy = display_strategies.get(display_type)

        if not strategy:
            raise ValueError(f"Unknown display type: {display_type}")

        strategy.display(self)

    def print_book(self, print_type: str) -> None:
        strategy = print_strategies.get(print_type)

        if not strategy:
            raise ValueError(f"Unknown print type: {print_type}")

        strategy.print_book(self)

    def serialize(self, serialize_type: str) -> str:
        serializer = serializers.get(serialize_type)

        if not serializer:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

        return serializer.serialize(self)
