# _변수_

> 변수란?

<br/>


[참조 :: 위키백과 - variable.](https://ko.wikipedia.org/wiki/%EB%B3%80%EC%88%98_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99)

<br/>

컴퓨터 프로그래밍에서 변수(變數, variable)는 아직 알려지지 않거나
어느 정도까지만 알려져 있는 양이나 정보에 대한 상징적인 이름이다.

<br/>

컴퓨터 소스 코드에서의 변수 이름은 일반적으로 데이터 저장 위치와
그 안의 내용물과 관련되어 있으며 이러한 것들은 프로그램 실행 도중에 변경될 수 있다.

<br/>

프로그래밍에서의 변수는 수학에서 말하는 변수의 개념과 완전히 일치하지 않을 수도 있다.

<br/>

컴퓨터 변수의 값은 수학에서처럼 등식이나 공식의 필수적인 부분이 아니다.

<br/>

컴퓨터 환경에서 변수는 반복적인 과정 안에서 이용할 수도 있다.

<br/>

이를테면 한 장소의 값을 할당한 뒤 어느 곳에서 사용한 다음
새로운 값으로 다시 할당하고 같은 방법으로 다시 사용할 수도 있다.

<br/>

컴퓨터 프로그래밍에서의 변수는 긴 이름이 자주 나오며,
어떻게 이용할 것인지에 대한 설명을 나타내는 반면
수학에서의 변수는 짧은 시간 동안 쓰이는 간결한 한 두 개 문자 이름이다.

<br/>

컴파일러는 변수의 상징적인 이름을 데이터의 실제 위치로 치환해야 한다.

<br/>

변수 값, 형, 위치는 일반적으로 고정된 채 유지되는 반면
위치에 저장되어 있는 데이터는 프로그램 실행 도중 변경될 수 있다.

<br/>

---

<br/>

# _변수 선언 방법_

> 변수 = 리터럴(값)

```python
foo = "this is foo"
print(foo) # this is foo

foo = 123
print(foo) # 123

foo = 123.456
print(foo) # 123.456
```

<br/>

---

<br/>

# _변수 이름 규칙_

**TODO** 변수이름규칙 camel, snake, pascal 정리해서 포스팅하기

<br/>

---

<br/>

# _다중 변수 초기화 하기_

```python
foo, bar, baz = "foo", "bar", "baz"
print(foo) # foo
print(bar) # bar
print(baz) # baz
```

<br/>

---

<br/>

# _다중 변수 리터럴 하나로 초기화 하기_

```python
foo = bar = baz = "this is variable."
print(foo) # this is variable.
print(bar) # this is variable.
print(baz) # this is variable.
```

<br/>

---

<br/>