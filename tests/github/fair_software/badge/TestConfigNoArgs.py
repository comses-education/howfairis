from tests.contracts.Config import Contract
import pytest
from tests.github.fair_software.badge.mocker import mocker
from howfairis import Config
from howfairis import Repo


@pytest.fixture
def mocked_config(mocker):
    with mocker:
        repo = Repo("https://github.com/fair-software/badge")
        return Config(repo)


class TestConfigNoArgs(Contract):

    def test_default(self, mocked_config):
        assert mocked_config.default == dict(force_repository=None, force_license=None, force_registry=None,
                                             force_citation=None, force_checklist=None, include_comments=False)

    def test_repo(self, mocked_config):
        assert mocked_config.repo == dict()

    def test_user(self, mocked_config):
        assert mocked_config.user == dict()
