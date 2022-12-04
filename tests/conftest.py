from pytest_factoryboy import register

from tests.factories import AdsFactory

pytest_plugins = 'tests.fixtures'


register(AdsFactory)
