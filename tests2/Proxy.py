from typing import final


class Demo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def m1(self, n):
        print(f"Hello from m1 with value {n}!")

    def m2(self):
        print("Hello from m2!")


class SimpleProxy:
    def __init__(self, target, rules: dict):
        object.__setattr__(self, "_SimpleProxy__target", target)
        object.__setattr__(self, "_SimpleProxy__rules", rules)

    def __check_args(self, method, args, kwargs):
        if args[0] not in self.__rules.get(method, []):
            return False
        return True

    def __getattr__(self, name):
        def methodWrapper(*args, **kwargs):
            if not self.__check_args(name, args, kwargs):
                raise ValueError(f"Недопустимые аргументы для метода {name}")
            return attr(*args, **kwargs)
        if name not in self.__rules:
            raise PermissionError(f"недостаточно прав для доступа к {name}!")
        attr = getattr(self.__target, name)
        if callable(attr):
            return methodWrapper
        else:
            return attr  # атрибуты без вызова (например, поля)

    def __dir__(self):
        result = []
        for attr in dir(self.__target):
            if (not attr.startswith("_")) and attr in self.__rules:
                result.append(attr)
        return result

    def __setattr__(self, name, value):
        raise AttributeError

    def __delattr__(self, name):
        raise AttributeError

    def __repr__(self):
        return f"<App>"

    def __str__(self):
        return str(self.__dir__())

    __dict__ = None
    __class__ = None
    __base__ = None
    __bases__ = None
    # __weakref__ = None


class FancyName(SimpleProxy):
    pass
