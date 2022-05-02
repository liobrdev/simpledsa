import pytest

from . import HashTable


@pytest.mark.parametrize('kwargs', [
    dict(first='first', second='second', third='third'),
    dict(first=1, second=2, third=3),
    dict(first=False, second=True, third=False),
    dict(first=(1, 'first'), second=(2, 'second'), third=(3, 'third')),
    dict(first={'first': 11}, second={'second': 22}, third={'third': 33}),
    dict(first=[10, 11], second=[21, 22], third=[32, 33]),
])
def test_initialize_hash_table_success(
    kwargs: dict[str, str | int | bool | tuple | dict | list],
):
    try:
        HashTable(**kwargs)
    except TypeError as e:
        assert False, f'Raised an exception: {e}'


@pytest.mark.parametrize('kwargs', [
    dict(first='first', second='second', third=3),
    dict(first=1, second=2, third='third'),
    dict(first=False, second='True', third=False),
    dict(first=[1, 'first'], second=(2, 'second'), third=(3, 'third')),
    dict(first={'first': 11}, second=('second', 22), third={'third': 33}),
    dict(first=[10, 11], second=[21, 22], third=(32, 33)),
])
def test_initialize_hash_table_fail(
    kwargs: dict[str, str | int | bool | tuple | dict | list],
):
    with pytest.raises(TypeError) as e:
        HashTable(**kwargs)

    assert 'All entries must have the same type!' in str(e.value)


def test_hash_table_len(
    example_hash_table_small: HashTable[str],
    example_hash_table_medium: HashTable[str],
    example_hash_table_large: HashTable[str],
):
    assert len(example_hash_table_small) == 2
    assert len(example_hash_table_medium) == 6
    assert len(example_hash_table_large) == 12


def test_hash_table_array_len(
    example_hash_table_small: HashTable[str],
    example_hash_table_medium: HashTable[str],
    example_hash_table_large: HashTable[str],
):
    assert len(example_hash_table_small._array) == 5
    assert len(example_hash_table_medium._array) == 13
    assert len(example_hash_table_large._array) == 29


def test_hash_table_get_success(example_hash_table_small: HashTable[str]):
    assert example_hash_table_small.get('first') == 'first@email.dev'
    assert example_hash_table_small.get('second') == 'second@email.dev'
    assert example_hash_table_small['first'] == 'first@email.dev'
    assert example_hash_table_small['second'] == 'second@email.dev'


def test_hash_table_get_fail_keyerror(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(KeyError) as e:
        example_hash_table_small.get('third')

    assert "Key 'third' not found!" in str(e.value)


def test_hash_table_get_fail_typeerror(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(TypeError) as e:
        example_hash_table_small.get('')

    assert 'Key must be a non-empty string!' in str(e.value)


def test_hash_table_put_success(example_hash_table_small: HashTable[str]):
    example_hash_table_small.put('third', 'third@email.dev')
    assert example_hash_table_small.get('third') == 'third@email.dev'


def test_hash_table_put_fail_valueerror(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(ValueError) as e:
        example_hash_table_small.put('second', 'another@email.dev')

    assert "Key 'second' already exists!" in str(e.value)


def test_hash_table_put_fail_typeerror_key(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(TypeError) as e:
        example_hash_table_small.put('', 'another@email.dev')

    assert 'Key must be a non-empty string!' in str(e.value)


def test_hash_table_put_fail_typeerror_value(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(TypeError) as e:
        example_hash_table_small.put('third', 3) # type: ignore

    assert "Value must be of type <class 'str'>!" in str(e.value)


def test_hash_table_update_success_call(
    example_hash_table_small: HashTable[str],
):
    assert example_hash_table_small.get('second') == 'second@email.dev'
    example_hash_table_small.update('second', 'updated@email.dev')
    assert example_hash_table_small.get('second') == 'updated@email.dev'


def test_hash_table_update_success_subscript(
    example_hash_table_small: HashTable[str],
):
    assert example_hash_table_small.get('second') == 'second@email.dev'
    example_hash_table_small['second'] = 'updated@email.dev'
    assert example_hash_table_small.get('second') == 'updated@email.dev'


def test_hash_table_update_fail_keyerror(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(KeyError) as e:
        example_hash_table_small.update('third', 'updated@email.dev')

    assert "Key 'third' not found!" in str(e.value)


def test_hash_table_update_fail_typeerror_key(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(TypeError) as e:
        example_hash_table_small.update('', 'updated@email.dev')

    assert 'Key must be a non-empty string!' in str(e.value)


def test_hash_table_update_fail_typeerror_value(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(TypeError) as e:
        example_hash_table_small.update('second', 2) # type: ignore

    assert "Value must be of type <class 'str'>!" in str(e.value)


def test_hash_table_delete_success_call(
    example_hash_table_small: HashTable[str],
):
    assert example_hash_table_small.get('second') == 'second@email.dev'
    example_hash_table_small.delete('second')

    with pytest.raises(KeyError) as e:
        example_hash_table_small.get('second')

    assert "Key 'second' not found!" in str(e.value)


def test_hash_table_delete_success_subscript(
    example_hash_table_small: HashTable[str],
):
    assert example_hash_table_small.get('second') == 'second@email.dev'
    del example_hash_table_small['second']

    with pytest.raises(KeyError) as e:
        example_hash_table_small.get('second')

    assert "Key 'second' not found!" in str(e.value)


def test_hash_table_delete_fail_keyerror(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(KeyError) as e:
        example_hash_table_small.delete('third')

    assert "Key 'third' not found!" in str(e.value)


def test_hash_table_delete_fail_typeerror(
    example_hash_table_small: HashTable[str],
):
    with pytest.raises(TypeError) as e:
        example_hash_table_small.delete('')

    assert 'Key must be a non-empty string!' in str(e.value)


def test_hash_table_expand_array_small(
    example_hash_table_small: HashTable[str],
):
    h = example_hash_table_small
    h.put('third', 'third@email.dev')
    assert h.get('third') == 'third@email.dev'
    assert len(h._array) == 5
    h.put('fourth', 'fourth@email.dev')
    assert h.get('fourth') == 'fourth@email.dev'
    assert len(h._array) == 13


def test_hash_table_expand_array_medium(
    example_hash_table_medium: HashTable[str],
):
    h = example_hash_table_medium

    for key in ['seventh', 'eighth']:
        h.put(key, f'{key}@email.dev')
        assert h.get(key) == f'{key}@email.dev'
        assert len(h._array) == 13

    h.put('ninth', 'ninth@email.dev')
    assert h.get('ninth') == 'ninth@email.dev'
    assert len(h._array) == 29


def test_hash_table_expand_array_large(
    example_hash_table_large: HashTable[str],
):
    h = example_hash_table_large

    for key in range(13, 20):
        h.put(f'{key}th', f'{key}th@email.dev')
        assert h.get(f'{key}th') == f'{key}th@email.dev'
        assert len(h._array) == 29

    h.put('20th', '20th@email.dev')
    assert h.get('20th') == '20th@email.dev'
    assert len(h._array) == 59


def test_hash_table_shrink_array_small(
    example_hash_table_small: HashTable[str],
):
    h = example_hash_table_small
    h.put('third', 'third@email.dev')
    assert len(h._array) == 5
    assert len([i for i in h._array if i == ()]) == 0
    assert len([i for i in h._array if i]) == 3

    assert h.get('third') == 'third@email.dev'
    h.delete('third')
    with pytest.raises(KeyError) as e:
        h.get('third')
    assert "Key 'third' not found!" in str(e.value)
    assert len(h._array) == 5
    assert len([i for i in h._array if i == ()]) == 1
    assert len([i for i in h._array if i]) == 2

    assert h.get('second') == 'second@email.dev'
    h.delete('second')
    with pytest.raises(KeyError) as e:
        h.get('second')
    assert "Key 'second' not found!" in str(e.value)
    assert len(h._array) == 5
    assert len([i for i in h._array if i == ()]) == 2
    assert len([i for i in h._array if i]) == 1

    assert h.get('first') == 'first@email.dev'
    h.delete('first')
    with pytest.raises(KeyError) as e:
        h.get('first')
    assert "Key 'first' not found!" in str(e.value)
    assert len(h._array) == 5
    assert len([i for i in h._array if i == ()]) == 3
    assert len([i for i in h._array if i]) == 0

    h.put('new_first', 'new_first@email.dev')
    assert h.get('new_first') == 'new_first@email.dev'
    assert len(h._array) == 13
    assert len([i for i in h._array if i == ()]) == 0
    assert len([i for i in h._array if i]) == 1

    h.put('new_second', 'new_second@email.dev')
    assert h.get('new_second') == 'new_second@email.dev'
    assert len(h._array) == 5
    assert len([i for i in h._array if i == ()]) == 0
    assert len([i for i in h._array if i]) == 2


def test_hash_table_shrink_array_medium(
    example_hash_table_medium: HashTable[str],
):
    h = example_hash_table_medium
    assert len(h._array) == 13
    assert len([i for i in h._array if i == ()]) == 0
    assert len([i for i in h._array if i]) == 6

    for n, key in enumerate(['sixth', 'fifth', 'fourth', 'third', 'second']):
        assert h.get(key) == f'{key}@email.dev'
        h.delete(key)
        with pytest.raises(KeyError) as e:
            h.get(key)
        assert f"Key '{key}' not found!" in str(e.value)
        array = h._array
        assert len(array) == 13
        assert len([i for i in array if i == ()]) == n + 1
        assert len([i for i in array if i]) == 6 - (n + 1)

    h.put('new_second', 'new_second@email.dev')
    assert h.get('new_second') == 'new_second@email.dev'
    assert len(h._array) == 5
    assert len([i for i in h._array if i == ()]) == 0
    assert len([i for i in h._array if i]) == 2


def test_hash_table_shrink_array_large(
    example_hash_table_large: HashTable[str],
):
    h = example_hash_table_large
    assert len(h._array) == 29
    assert len([i for i in h._array if i == ()]) == 0
    assert len([i for i in h._array if i]) == 12

    for n, key in enumerate([
        'twelfth', 'eleventh', 'tenth', 'ninth', 'eighth', 'seventh', 'sixth',
        'fifth', 'fourth',
    ]):
        assert h.get(key) == f'{key}@email.dev'
        h.delete(key)
        with pytest.raises(KeyError) as e:
            h.get(key)
        assert f"Key '{key}' not found!" in str(e.value)
        array = h._array
        assert len(array) == 29
        assert len([i for i in array if i == ()]) == n + 1
        assert len([i for i in array if i]) == 12 - (n + 1)

    h.put('new_fourth', 'new_fourth@email.dev')
    assert h.get('new_fourth') == 'new_fourth@email.dev'
    assert len(h._array) == 11
    assert len([i for i in h._array if i == ()]) == 0
    assert len([i for i in h._array if i]) == 4

