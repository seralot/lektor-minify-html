import pytest
from lektor_minify_html import MinifyHtmlPlugin
from lektor.project import Project

@pytest.fixture
def env():
    project = Project.discover("example-project")
    return project.make_env()

@pytest.fixture()
def plugin(env):
    return MinifyHtmlPlugin(env, "minify-html")
