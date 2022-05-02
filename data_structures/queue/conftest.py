import pytest

from . import Queue


@pytest.fixture
def example_queue_small() -> Queue[str]:
    return Queue('first', 'second')


@pytest.fixture
def example_queue_medium() -> Queue[str]:
    return Queue(
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth',)


@pytest.fixture
def example_queue_large() -> Queue[str]:
    return Queue(
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth',)

