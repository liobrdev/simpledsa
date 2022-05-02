import pytest

from . import Stack


@pytest.fixture
def example_stack_small() -> Stack[str]:
    return Stack('first', 'second')


@pytest.fixture
def example_stack_medium() -> Stack[str]:
    return Stack(
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth',)


@pytest.fixture
def example_stack_large() -> Stack[str]:
    return Stack(
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth',)

