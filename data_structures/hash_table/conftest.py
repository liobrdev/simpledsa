import pytest

from . import HashTable


@pytest.fixture
def example_hash_table_small() -> HashTable[str]:
    return HashTable(first='first@email.dev', second='second@email.dev')


@pytest.fixture
def example_hash_table_medium() -> HashTable[str]:
    return HashTable(
        first='first@email.dev', second='second@email.dev',
        third='third@email.dev', fourth='fourth@email.dev',
        fifth='fifth@email.dev', sixth='sixth@email.dev',)


@pytest.fixture
def example_hash_table_large() -> HashTable[str]:
    return HashTable(
        first='first@email.dev', second='second@email.dev',
        third='third@email.dev', fourth='fourth@email.dev',
        fifth='fifth@email.dev', sixth='sixth@email.dev',
        seventh='seventh@email.dev', eighth='eighth@email.dev',
        ninth='ninth@email.dev', tenth='tenth@email.dev',
        eleventh='eleventh@email.dev', twelfth='twelfth@email.dev',)

