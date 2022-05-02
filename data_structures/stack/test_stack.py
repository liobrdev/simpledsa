from pytest import mark, raises, CaptureFixture

from . import Stack


@mark.parametrize('args', [
    ['first', 'second', 'third'],
    [1, 2, 3],
    [False, True, False],
    [(1, 'first'), (2, 'second'), (3, 'third')],
    [{'first': 11}, {'second': 22}, {'third': 33}],
    [[10, 11], [21, 22], [32, 33]],
])
def test_initialize_stack_success(
    args: list[str | int | bool | tuple | dict | list],
):
    Stack(*args)


@mark.parametrize('args', [
    ['first', 'second', 3],
    [1, 2, 'third'],
    [False, 'True', False],
    [[1, 'first'], (2, 'second'), (3, 'third')],
    [{'first': 11}, ('second', 22), {'third': 33}],
    [[10, 11], [21, 22], (32, 33)],
])
def test_initialize_stack_fail(
    args: list[str | int | bool | tuple | dict | list],
):
    with raises(TypeError) as e:
        Stack(*args)

    assert 'All entries must have the same type!' in str(e.value)


def test_stack_repr(
    capsys: CaptureFixture[str],
    example_stack_small: Stack[str],
):
    print(example_stack_small)
    captured = capsys.readouterr()
    assert captured.out == "['first', 'second']\n"


def test_stack_len(
    example_stack_small: Stack[str],
    example_stack_medium: Stack[str],
    example_stack_large: Stack[str],
):
    assert len(example_stack_small) == 2
    assert len(example_stack_medium) == 6
    assert len(example_stack_large) == 12


def test_stack_push_success():
    s = Stack()
    assert len(s) == 0
    assert str(s) == "[]"
    assert s._data_type == None
    s.push('first')
    assert len(s) == 1
    assert str(s) == "['first']"
    assert s._data_type == str
    s.push('second')
    assert len(s) == 2
    assert str(s) == "['first', 'second']"


def test_stack_push_fail_typeerror(example_stack_small: Stack[str]):
    with raises(TypeError) as e:
        example_stack_small.push(100) # type: ignore

    assert "Value must be of type <class 'str'>!" in str(e.value)


def test_stack_pop_success(example_stack_small: Stack[str]):
    assert len(example_stack_small) == 2
    assert str(example_stack_small) == "['first', 'second']"
    assert example_stack_small.pop() == 'second'
    assert len(example_stack_small) == 1
    assert str(example_stack_small) == "['first']"
    assert example_stack_small.pop() == 'first'
    assert len(example_stack_small) == 0
    assert str(example_stack_small) == "[]"

    with raises(RuntimeError) as e:
        example_stack_small.pop()

    assert 'Underflow - stack is empty!' in str(e.value)


def test_stack_top_success(example_stack_small: Stack[str]):
    assert example_stack_small.top() == 'second'
    assert example_stack_small.pop() == 'second'
    assert example_stack_small.top() == 'first'
    assert example_stack_small.pop() == 'first'

    with raises(RuntimeError) as e:
        example_stack_small.top()

    assert 'Underflow - stack is empty!' in str(e.value)


def test_stack_is_empty(example_stack_small: Stack[str]):
    assert example_stack_small.is_empty() == False
    assert example_stack_small.pop() == 'second'
    assert example_stack_small.is_empty() == False
    assert example_stack_small.pop() == 'first'
    assert example_stack_small.is_empty() == True
    example_stack_small.push('new_first')
    assert example_stack_small.is_empty() == False


def test_stack_copy_success(example_stack_small: Stack[str]):
    s = example_stack_small
    t = s.copy()
    assert str(s) == str(t)
    assert s is not t
    assert s._top is not t._top
    assert s._top and t._top and s._top.next is not t._top.next

