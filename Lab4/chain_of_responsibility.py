from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class SummatorHandler(AbstractHandler):

    def handle(self, request: Any) -> str:
        if request.startswith('сложить'):
            req_list = []
            req_list = request.split()
            return f"Результат операции: {int(req_list[1]) + int(req_list[3])}"
        else:
            return super().handle(request)


class SubtractorHandler(AbstractHandler):

    def handle(self, request: Any) -> str:
        if request.startswith('вычесть'):
            req_list = []
            req_list = request.split()
            return f"Результат операции: {int(req_list[3]) - int(req_list[1])}"
        else:
            return super().handle(request)


class MultiplierHandler(AbstractHandler):

    def handle(self, request: Any) -> str:
        if request.startswith('умножить'):
            req_list = []
            req_list = request.split()
            return f"Результат операции: {int(req_list[1]) * int(req_list[3])}"
        else:
            return super().handle(request)


class DivisorHandler(AbstractHandler):

    def handle(self, request: Any) -> str:
        if request.startswith('поделить'):
            req_list = []
            req_list = request.split()
            return f"Результат операции: {float(req_list[1]) / float(req_list[3])}"
        else:
            return super().handle(request)



if __name__ == "__main__":

    summator = SummatorHandler()
    subtractor = SubtractorHandler()
    multiplier = MultiplierHandler()
    divisor = DivisorHandler()

    summator.set_next(subtractor).set_next(multiplier).set_next(divisor)

    print('\n')
    for op in ["умножить 5 на 3", "поделить 25 на 10", "вычесть 12 из 22", "сложить 77 и 33", "возвести 2 в 6 степень"]:
        result = summator.handle(op)
        print(f"Операция: {op}")
        if result:
            print(f"{result}")
        else:
            print(f"Операция не была выполнена.")
        print('\n')