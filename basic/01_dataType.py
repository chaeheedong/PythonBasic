




# 자료형
foo = None         # NoneType
foo = "string"     # str
foo = b"12345"     # bytes
foo = bytearray(5) # bytearray
foo = memoryview(bytes(5)) # memoryview
foo = 1            # int
foo = 1.1          # float
foo = 1j           # complex
foo = True         # bool
# ===========================


# 자료형(집합형)
foo = ["FOO", "BAR", "BAZ"]      # list
foo = ("FOO", "BAR", "BAZ")      # tuple
foo = range(5)                   # range
foo = {"name": "FOO", "age": 10} # dict
foo = {"FOO", "BAR", "BAZ"}      # set
foo = frozenset({"FOO", "BAR"})  # frozenset
# ===========================

# 자료형 확인하기
print("자료형 확인하기")
foo = None
print("foo = None", type(foo)) # NoneType

foo = "string"
print('foo = "string"', type(foo)) # str

foo = b"12345"
print('foo = b"12345"', type(foo)) # bytes

foo = bytearray(5)
print("foo = bytearray(5)", type(foo)) # bytearray

foo = memoryview(bytes(5))
print("foo = memoryview(bytes(5))", type(foo)) # memoryview

foo = 1
print("foo = 1", type(foo)) # int

foo = 1.1
print("foo = 1.1", type(foo)) # float

foo = 1j
print("foo = 1j", type(foo)) # complex

foo = True
print("foo = True", type(foo)) # bool

foo = ["FOO", "BAR", "BAZ"]
print('foo = ["FOO", "BAR", "BAZ"]', type(foo)) # list

foo = ("FOO", "BAR", "BAZ")
print('foo = ("FOO", "BAR", "BAZ")', type(foo)) # tuple

foo = range(5)
print("foo = range(5)", type(foo)) # range

foo = {"name": "FOO", "age": 10}
print('foo = {"name": "FOO", "age": 10}', type(foo)) # dict

foo = {"FOO", "BAR", "BAZ"}
print('foo = {"FOO", "BAR", "BAZ"}', type(foo)) # set

foo = frozenset({"FOO", "BAR"})
print('foo = frozenset({"FOO", "BAR"})', type(foo)) # frozenset
# ===========================