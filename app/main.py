from abc import ABC


class IntegerRange:
    """ class - descriptor for parameters limitations """
    def __init__(self, min_amount: int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner: type, name: str) -> None:
        self.protected_name = "_" + name

    def __get__(self, instance: object, owner: type) -> None:
        return getattr(instance, self.protected_name)

    def __set__(self, instance: object, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Value should be integer!")
        if not self.min_amount <= value <= self.max_amount:
            raise ValueError("Value is out of allowed range!")
        setattr(instance, self.protected_name, value)


class Visitor:
    """  class that is responsible for the user's personal data  """
    def __init__(self, name: str, age: int, weight: int, height: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self, age: int, weight: int, height: int) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    """  it's a limitation class validators for slides  """
    age = IntegerRange(4, 14)
    height = IntegerRange(80, 120)
    weight = IntegerRange(20, 50)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    """  it's a limitation class validators for slides  """
    age = IntegerRange(14, 60)
    height = IntegerRange(120, 220)
    weight = IntegerRange(50, 120)


class Slide:
    def __init__(
            self,
            name: str,
            limitation_class: SlideLimitationValidator
    ) -> None:
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, client: Visitor) -> bool:
        """  checks whether a Visitor can use the slide  """
        try:
            self.limitation_class(age=client.age,
                                  height=client.height,
                                  weight=client.weight)
            return True
        except ValueError:
            return False
