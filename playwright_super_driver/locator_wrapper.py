from playwright._impl._locator import Locator as LocatorOrigin


class Locator():
    def __init__(self, locator) -> None:
        self._locator: LocatorOrigin = locator

    def fill(self, value: str):
        self._locator.fill(value)

    def click(self):
        self._locator.click()

    def count(self):
        return self._locator.count()

    def exists(self):
        return bool(self.count())

    def is_visible(self):
        return self._locator.is_visible()

    def is_enabled(self):
        return self._locator.is_enabled()

    def inner_text(self) -> str:
        return self._locator.inner_text()

    def locator(self, selector: str):
        return Locator(self._locator.locator(selector))

    def first(self):
        return Locator(self._locator.first)

    def nth(self, index: int):
        return Locator(self._locator.nth(index))

    def to_list(self) -> list:
        l = []
        for i in range(0, self.count()):
            l.append(self.nth(i))
        return l
