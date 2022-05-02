from pytest import mark, raises, CaptureFixture, MonkeyPatch
from typing import Optional

from . import LinkedList


@mark.parametrize('args', [
    ['first', 'second', 'third'],
    [1, 2, 3],
    [False, True, False],
    [(1, 'first'), (2, 'second'), (3, 'third')],
    [{'first': 11}, {'second': 22}, {'third': 33}],
    [[10, 11], [21, 22], [32, 33]],
])
def test_initialize_linked_list_success(
    args: list[str | int | bool | tuple | dict | list],
):
    LinkedList(*args)


@mark.parametrize('args', [
    ['first', 'second', 3],
    [1, 2, 'third'],
    [False, 'True', False],
    [[1, 'first'], (2, 'second'), (3, 'third')],
    [{'first': 11}, ('second', 22), {'third': 33}],
    [[10, 11], [21, 22], (32, 33)],
])
def test_initialize_linked_list_fail(
    args: list[str | int | bool | tuple | dict | list],
):
    with raises(TypeError) as e:
        LinkedList(*args)

    assert 'All entries must have the same type!' in str(e.value)


def test_linked_list_repr(
    capsys: CaptureFixture[str],
    example_linked_list_small: LinkedList[str],
):
    print(example_linked_list_small)
    captured = capsys.readouterr()
    assert captured.out == "['first', 'second']\n"


def test_linked_list_len(
    example_linked_list_small: LinkedList[str],
    example_linked_list_medium: LinkedList[str],
    example_linked_list_large: LinkedList[str],
):
    assert len(example_linked_list_small) == 2
    assert len(example_linked_list_medium) == 6
    assert len(example_linked_list_large) == 12


def test_linked_list_insert_success_already_occupied(
    capsys: CaptureFixture[str],
    example_linked_list_small: LinkedList[str],
):
    l = example_linked_list_small
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['first', 'second']\n"
    assert len(l) == 2
    assert l._head and l._head.data == 'first'
    l.insert('zero')
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['zero', 'first', 'second']\n"
    assert len(l) == 3
    assert l._head and l._head.data == 'zero'
    l.insert('third', 3)
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['zero', 'first', 'second', 'third']\n"
    assert len(l) == 4
    assert l._head and l._head.data == 'zero'
    l.insert('1.5th', 2)
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['zero', 'first', '1.5th', 'second', 'third']\n"
    assert len(l) == 5
    assert l._head and l._head.data == 'zero'


def test_linked_list_insert_success_empty(capsys: CaptureFixture[str]):
    l: LinkedList[str] = LinkedList()
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "[]\n"
    l.insert('first')
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['first']\n"
    assert len(l) == 1
    assert l._head and l._head.data == 'first'


def test_linked_list_insert_fail_typeerror_data(
    example_linked_list_small: LinkedList[str],
):
    with raises(TypeError) as e:
        example_linked_list_small.insert(100) # type: ignore

    assert "Value must be of type <class 'str'>!" in str(e.value)


def test_linked_list_insert_fail_typeerror_index(
    example_linked_list_small: LinkedList[str],
):
    with raises(TypeError) as e:
        example_linked_list_small.insert('third', 'two') # type: ignore

    assert 'Index must be an integer!' in str(e.value)


def test_linked_list_append_success_already_occupied(
    capsys: CaptureFixture[str],
    example_linked_list_small: LinkedList[str],
):
    l = example_linked_list_small
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['first', 'second']\n"
    assert len(l) == 2
    l.append('third')
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['first', 'second', 'third']\n"
    assert len(l) == 3


def test_linked_list_append_success_empty(capsys: CaptureFixture[str]):
    l: LinkedList[str] = LinkedList()
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "[]\n"
    l.append('first')
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['first']\n"
    assert len(l) == 1
    assert l._head and l._head.data == 'first'


def test_linked_list_append_fail_typeerror(
    example_linked_list_small: LinkedList[str],
):
    with raises(TypeError) as e:
        example_linked_list_small.append(100) # type: ignore

    assert "Value must be of type <class 'str'>!" in str(e.value)


def test_linked_list_reverse(
    capsys: CaptureFixture[str],
    example_linked_list_medium: LinkedList[str],
):
    l = example_linked_list_medium
    print(l)
    captured = capsys.readouterr()
    assert captured.out == \
        "['first', 'second', 'third', 'fourth', 'fifth', 'sixth']\n"
    assert l._head and l._head.data == 'first'
    l.reverse()
    print(l)
    captured = capsys.readouterr()
    assert captured.out == \
        "['sixth', 'fifth', 'fourth', 'third', 'second', 'first']\n"
    assert l._head and l._head.data == 'sixth'


def test_linked_list_traverse_success(
    monkeypatch: MonkeyPatch,
    example_linked_list_medium: LinkedList[str],
):
    l = example_linked_list_medium

    def mock_input(message: str):
        assert message == 'Press Enter to view NEXT node (^C to exit):\n'
        return ''

    def mock_print(message: str):
        return message

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr('builtins.print', mock_print)
    end_message: str = l.traverse()
    assert end_message == 'End of linked list.'


def test_linked_list_traverse_no_head(monkeypatch: MonkeyPatch):
    l: LinkedList[str] = LinkedList()

    def mock_print(message: str):
        return message

    monkeypatch.setattr('builtins.print', mock_print)
    end_message: str = l.traverse()
    assert end_message == 'No HEAD node.'


def test_linked_list_find_success(example_linked_list_small: LinkedList[str]):
    l = example_linked_list_small
    result = l.find('second')
    assert result['data'] == 'second'
    assert result['index'] == 1
    assert l._head and result['node'] == hex(id(l._head.next))


def test_linked_list_find_fail_valueerror(
    example_linked_list_small: LinkedList[str],
):
    with raises(ValueError) as e:
        example_linked_list_small.find('third')

    assert "'third' is not in linked list!" in str(e.value)


def test_linked_list_delete_success(
    capsys: CaptureFixture[str],
    example_linked_list_medium: LinkedList[str],
):
    l = example_linked_list_medium
    assert len(l) == 6

    result_1 = l.find('first')
    assert result_1['data'] == 'first'
    assert result_1['index'] == 0
    assert result_1['node'] == hex(id(l._head))

    l.delete('first')
    with raises(ValueError) as e:
        l.find('first')
    assert "'first' is not in linked list!" in str(e.value)
    assert len(l) == 5
    result_2 = l.find('second')
    assert result_2['data'] == 'second'
    assert result_2['index'] == 0
    assert result_2['node'] == hex(id(l._head))

    l.delete('sixth')
    with raises(ValueError) as e:
        l.find('sixth')
    assert "'sixth' is not in linked list!" in str(e.value)
    assert len(l) == 4

    l.delete('fourth')
    with raises(ValueError) as e:
        l.find('fourth')
    assert "'fourth' is not in linked list!" in str(e.value)
    assert len(l) == 3
    print(l)
    captured = capsys.readouterr()
    assert captured.out == "['second', 'third', 'fifth']\n"


def test_linked_list_delete_fail_valueerror(
    example_linked_list_small: LinkedList[str],
):
    with raises(ValueError) as e:
        example_linked_list_small.delete('third')

    assert "'third' is not in linked list!" in str(e.value)


def test_linked_list_update_success(
    example_linked_list_small: LinkedList[str],
):
    l = example_linked_list_small
    result_1 = l.find('first')
    assert result_1['data'] == 'first'
    assert result_1['index'] == 0
    assert result_1['node'] == hex(id(l._head))
    assert str(l) == "['first', 'second']"

    l.update('first', 'updated_first')
    with raises(ValueError) as e:
        l.find('first')
    assert "'first' is not in linked list!" in str(e.value)

    result_2 = l.find('updated_first')
    assert result_2['data'] == 'updated_first'
    assert result_2['index'] == 0
    assert result_2['node'] == hex(id(l._head))
    assert str(l) == "['updated_first', 'second']"


def test_linked_list_update_fail_valueerror(
    example_linked_list_small: LinkedList[str],
):
    with raises(ValueError) as e:
        example_linked_list_small.update('third', 'updated_third')

    assert "'third' is not in linked list!" in str(e.value)


def test_linked_list_add_ll_success(
    example_linked_list_small: LinkedList[str],
):
    l = example_linked_list_small
    other = LinkedList('third', 'fourth')
    empty_1: LinkedList[str] = LinkedList()
    empty_2: LinkedList[str] = LinkedList()
    assert str(l) == "['first', 'second']"
    assert str(other) == "['third', 'fourth']"
    assert str(empty_1 + empty_2) == "[]"
    assert str(empty_1 + l) == str(l)
    assert str(l + empty_1) == str(l)
    assert str(l + other) == "['first', 'second', 'third', 'fourth']"
    assert str(empty_1) == "[]"
    assert str(empty_2) == "[]"
    assert str(l) == "['first', 'second']"
    assert str(other) == "['third', 'fourth']"


def test_linked_list_copy_success(example_linked_list_small: LinkedList[str]):
    l = example_linked_list_small
    m = l.copy()
    assert str(l) == str(m)
    assert l is not m
    assert l._head is not m._head
    assert \
        l._head and m._head and l._head.next is not m._head.next


@mark.parametrize('arg_1, arg_2', [
    ('first', 1),
    (1, False),
    (False, 'True'),
    ((2, 'second'), {'first': 11}),
    ({'second': 22}, ['third']),
    ([10, 11], (21, 22)),
    (None, False)
])
def test_linked_list_add_ll_fail_typeerror(
    arg_1: Optional[str | int | bool | tuple | dict | list],
    arg_2: Optional[str | int | bool | tuple | dict | list],
):
    list_1 = LinkedList(arg_1)
    list_2 = LinkedList(arg_2)

    with raises(TypeError) as e:
        list_1 + list_2

    assert (
        'Cannot merge linked lists with different data types:' +
        f" '{list_1._data_type}' and" +
        f" '{list_2._data_type}'"
    ) in str(e.value)


@mark.parametrize('sequence', [['third', 'fourth'], ('third', 'fourth')])
def test_linked_list_add_sequence_success(
    sequence: list | tuple,
    example_linked_list_small: LinkedList[str],
):
    l = example_linked_list_small
    sequence = ['third', 'fourth']
    assert str(l) == "['first', 'second']"
    assert str(sequence) == "['third', 'fourth']"
    assert str(l + []) == str(l)
    assert str(l + ()) == str(l)
    assert str(l) == "['first', 'second']"
    assert str(l + sequence) == "['first', 'second', 'third', 'fourth']"
    assert str(l) == "['first', 'second']"
    assert str(sequence) == "['third', 'fourth']"


@mark.parametrize('other', ['third', 3, False, { 'second': 22 }, None])
def test_linked_list_add_nonsequence_fail_typeerror(
    other: Optional[str | int | bool | dict],
    example_linked_list_small: LinkedList[str],
):
    l = example_linked_list_small

    with raises(TypeError) as e:
        l + other

    assert (
        'Unsupported operand type(s) for +:' +
        f" '{type(l)}' and '{type(other)}'"
    ) in str(e.value)


@mark.parametrize('data, sequence', [
    ('first', ['third', 21]),
    (200, ['third', 21]),
    (True, (False, 'fourth')),
    (('second', 90), (False, 'fourth')),
    ({'item': 200}, [{'third': 3}, 21]),
    ([111, 100], [{'third': 3}, [211]]),
])
def test_linked_list_add_sequence_fail_typeerror(
    data: Optional[str | int | bool | tuple | dict | list],
    sequence: list | tuple,
):
    l = LinkedList(data)

    with raises(TypeError) as e:
        l + sequence

    assert l._head and (
        f"Appended items must be of type '{type(l._head.data)}'"
    ) in str(e.value)


def test_linked_list_eq_ne(example_linked_list_small: LinkedList[str]):
    other_1 = LinkedList('first', 'second')
    other_2 = LinkedList(1, 2)
    assert example_linked_list_small == other_1
    assert other_1 != other_2

