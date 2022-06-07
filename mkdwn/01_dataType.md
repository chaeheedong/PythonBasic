# 자료형

## 목차

---

- 자료형
- 자료형(기본)
- 자료형(집합형)
- 자료형 확인

---

<br/><br/><br/>

### 자료형

---

[참조 :: 위키백과 - 파이썬 자료형](https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC#%EC%9E%90%EB%A3%8C%ED%98%95)

파이썬은 다음과 같은 자료형들을 갖고 있다.

기본 자료형:  
정수형  
긴 정수형(long integer)  
부동소수점형  
복소수형  
문자형  
유니코드 문자형  
함수형  
논리형(boolean)

집합형 자료형:  
리스트형 - 내부의 값을 나중에 바꿀 수 있다.  
튜플(tuple)형 - 한 번 값을 정하면 내부의 값을 바꿀 수 없다.  
사전형 - 내부의 값을 나중에 바꿀 수 있다.  
집합형 - 중복을 허락하지 않는다. 변경 가능하게도, 변경 불가능하게도 만들 수 있다.  
또 많은 객체 지향 언어와 같이, 사용자가 새롭게 자신의 형을 정의할 수도 있다.

<br/><br/><br/>

### 자료형(기본)

---

```python
foo = None         # NoneType
foo = "string"     # str
foo = b"12345"     # bytes
foo = bytearray(5) # bytearray
foo = memoryview(bytes(5)) # memoryview
foo = 1            # int
foo = 1.1          # float
foo = 1j           # complex
foo = True         # bool
```

<br/><br/><br/>

### 자료형(집합형)

---

```python
foo = ["FOO", "BAR", "BAZ"]      # list
foo = ("FOO", "BAR", "BAZ")      # tuple
foo = range(5)                   # range
foo = {"name": "FOO", "age": 10} # dict
foo = {"FOO", "BAR", "BAZ"}      # set
foo = frozenset({"FOO", "BAR"})  # frozenset
```

<br/><br/><br/>


### 자료형 확인

---

- 자료형을 확인 하려면 type 함수를 이용하면 된다.

```python
foo = None
print(type(foo)) # NoneType

foo = "string"
print(type(foo)) # str

foo = b"12345"
print(type(foo)) # bytes

foo = bytearray(5)
print(type(foo)) # bytearray

foo = memoryview(bytes(5))
print(type(foo)) # memoryview

foo = 1
print(type(foo)) # int

foo = 1.1
print(type(foo)) # float

foo = 1j
print(type(foo)) # complex

foo = True
print(type(foo)) # bool

foo = ["FOO", "BAR", "BAZ"]
print(type(foo)) # list

foo = ("FOO", "BAR", "BAZ")
print(type(foo)) # tuple

foo = range(5)
print(type(foo)) # range

foo = {"name": "FOO", "age": 10}
print(type(foo)) # dict

foo = {"FOO", "BAR", "BAZ"}
print(type(foo)) # set

foo = frozenset({"FOO", "BAR"})
print(type(foo)) # frozenset
```
