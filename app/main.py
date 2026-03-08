import json
import xml.etree.ElementTree as ElementTree


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


class DisplayStrategy:
    def display(self, book: Book) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


display_strategies = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}


class PrintStrategy:
    def print_book(self, book: Book) -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


print_strategies = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}


class SerializeStrategy:
    def serialize(self, book: Book) -> str:
        raise NotImplementedError


class JSONSerializer(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")


serializers = {
    "json": JSONSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
