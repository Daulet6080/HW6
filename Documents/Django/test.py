from typing import (
    Union,
    Optional,
    Any,
    List,
    Tuple,
    Dict,
    Set,
    Sequence,
    Iterable,
    Mapping,
    Callable,
    TypeVar,
    TypedDict,
    NamedTuple,
    Literal,
    NoReturn,
)


class UNION:
    def union( x: list[int] , y: list[int] ) -> list[int]:
        return list(set(x) | set(y))
    
print(UNION.union([2,3,4,8,9], [2,3,4,5]))

class OPTIONAL:
    
    def divide(x:int,y: Optional[int]) -> int:
        if y==0:
            return None
        return x/y
print(OPTIONAL.divide(10,2))


class Book:
    def init(self, title: str, author: Optional[str] = None):
        self.title = title
        self.author = author

    def str(self) -> str:
        if self.author is None:
            return f"{self.title} - Автор белгісіз"
        return f"{self.title} - {self.author}"

b1 = Book("Python Basics", "Guido van Rossum")
b2 = Book("Unknown Book")

print(b1)
print(b2)


"""Any"""
def data(text: any):
    return text


"""List examples"""

def sum(nums: list[int]) -> int:
    total = 0
    for n in nums:
        total +=n
    return total


num = [3, 7, -2, 9, 5]
print(sum(num))

def max_num(num: list[int]) -> int:
    min = num[0]
    for m in num:
        if m > min:
            min = m
    return min
    
        
print(max_num(num))



def remove_words(words: list[str]) -> list[str]:
    unique = []
    for w in words:
        if w not in unique:
            unique.append(w)
    return unique
            

words = ["apple", "banana", "cherry", "apple", "date", "banana"]
print(remove_words(words))


"""Sequense"""
