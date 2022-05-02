import pytest

from . import LinkedList


@pytest.fixture
def example_linked_list_small() -> LinkedList[str]:
    return LinkedList('first', 'second')


@pytest.fixture
def example_linked_list_medium() -> LinkedList[str]:
    return LinkedList(
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth',)


@pytest.fixture
def example_linked_list_large() -> LinkedList[str]:
    return LinkedList(
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth',)

