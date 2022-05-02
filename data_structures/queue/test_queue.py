from pytest import mark, raises, CaptureFixture

from . import Queue


@mark.parametrize('args', [
    ['first', 'second', 'third'],
    [1, 2, 3],
    [False, True, False],
    [(1, 'first'), (2, 'second'), (3, 'third')],
    [{'first': 11}, {'second': 22}, {'third': 33}],
    [[10, 11], [21, 22], [32, 33]],
])
def test_initialize_queue_success(
    args: list[str | int | bool | tuple | dict | list],
):
    Queue(*args)


@mark.parametrize('args', [
    ['first', 'second', 3],
    [1, 2, 'third'],
    [False, 'True', False],
    [[1, 'first'], (2, 'second'), (3, 'third')],
    [{'first': 11}, ('second', 22), {'third': 33}],
    [[10, 11], [21, 22], (32, 33)],
])
def test_initialize_queue_fail(
    args: list[str | int | bool | tuple | dict | list],
):
    with raises(TypeError) as e:
        Queue(*args)

    assert 'All entries must have the same type!' in str(e.value)


def test_queue_repr(
    capsys: CaptureFixture[str],
    example_queue_small: Queue[str],
):
    print(example_queue_small)
    captured = capsys.readouterr()
    assert captured.out == "['first', 'second']\n"


def test_queue_len(
    example_queue_small: Queue[str],
    example_queue_medium: Queue[str],
    example_queue_large: Queue[str],
):
    assert len(example_queue_small) == 2
    assert len(example_queue_medium) == 6
    assert len(example_queue_large) == 12


def test_queue_enqueue_success():
    q = Queue()
    assert len(q) == 0
    assert str(q) == "[]"
    assert q._data_type == None
    assert q._front == None
    assert q._rear == None
    q.enqueue('first')
    assert len(q) == 1
    assert str(q) == "['first']"
    assert q._data_type == str
    assert q._front.data == 'first'
    assert q._rear.data == 'first'
    q.enqueue('second')
    assert len(q) == 2
    assert str(q) == "['first', 'second']"
    assert q._front.data == 'first'
    assert q._rear.data == 'second'


def test_queue_enqueue_fail_typeerror(example_queue_small: Queue[str]):
    with raises(TypeError) as e:
        example_queue_small.enqueue(100) # type: ignore

    assert "Value must be of type <class 'str'>!" in str(e.value)


def test_queue_dequeue_success(example_queue_small: Queue[str]):
    assert len(example_queue_small) == 2
    assert str(example_queue_small) == "['first', 'second']"
    assert example_queue_small.dequeue() == 'first'
    assert len(example_queue_small) == 1
    assert str(example_queue_small) == "['second']"
    assert example_queue_small.dequeue() == 'second'
    assert len(example_queue_small) == 0
    assert str(example_queue_small) == "[]"

    with raises(RuntimeError) as e:
        example_queue_small.dequeue()

    assert 'Queue is empty!' in str(e.value)


def test_queue_front_success(example_queue_small: Queue[str]):
    assert example_queue_small.front() == 'first'
    assert example_queue_small.dequeue() == 'first'
    assert example_queue_small.front() == 'second'
    assert example_queue_small.dequeue() == 'second'

    with raises(RuntimeError) as e:
        example_queue_small.front()

    assert 'Queue is empty!' in str(e.value)


def test_queue_rear_success(example_queue_small: Queue[str]):
    assert example_queue_small.rear() == 'second'
    example_queue_small.enqueue('third')
    assert example_queue_small.rear() == 'third'
    example_queue_small.enqueue('fourth')
    assert example_queue_small.rear() == 'fourth'


def test_queue_front_rear_empty():
    q = Queue()

    with raises(RuntimeError) as e:
        q.front()
    assert 'Queue is empty!' in str(e.value)

    with raises(RuntimeError) as e:
        q.rear()
    assert 'Queue is empty!' in str(e.value)

    q.enqueue('first')
    assert q.front() == 'first'
    assert q.rear() == 'first'
    q.enqueue('second')
    assert q.front() == 'first'
    assert q.rear() == 'second'
    assert q.dequeue() == 'first'
    assert q.front() == 'second'
    assert q.rear() == 'second'
    assert q.dequeue() == 'second'

    with raises(RuntimeError) as e:
        q.front()
    assert 'Queue is empty!' in str(e.value)

    with raises(RuntimeError) as e:
        q.rear()
    assert 'Queue is empty!' in str(e.value)


def test_queue_is_empty():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue('first')
    assert q.is_empty() == False
    assert q.dequeue() == 'first'
    assert q.is_empty() == True


def test_queue_copy_success(example_queue_small: Queue[str]):
    q = example_queue_small
    r = q.copy()
    assert str(q) == str(r)
    assert q is not r
    assert q._front is not r._front
    assert q._front and r._front and q._front.next is not r._front.next
    assert q._rear is not r._rear
    assert q._rear and q._rear.next is None
    assert r._rear and r._rear.next is None

