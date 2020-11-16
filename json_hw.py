class JsonConverter:
    def __init__(self, mapping: dict):
        if not isinstance(mapping, dict):
            raise TypeError
        for each in mapping:
            setattr(self, each, mapping[each])
            if isinstance(mapping[each], dict):
                setattr(self, each, JsonConverter(mapping[each]))

    def __repr__(self):
        return f"{self.__dict__}"


class ColorizeMixin:
    repr_color_code = 32

    def reproduce(self, text):
        return f"\033[1;{self.repr_color_code};40m {text}"


class Advert(ColorizeMixin, JsonConverter):
    def __init__(self, mapping):
        super().__init__(mapping)
        try:
            try:
                if self.price < 0:
                    raise ValueError
            except ValueError:
                print("ValueError: price must be not less than 0")
        except AttributeError:
            self.price = 0

    def __repr__(self):
        return super().reproduce(f"{self.title} | {self.price} ₽")


if __name__ == "__main__":
    import json

    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    ad = Advert(lesson)
    print(ad)
