from gocept.jenkinsdsl.jenkinsdsl import Handler


CAUTION = '// *Caution:* Do not change'
VCS_INTERFACE = 'interface VersionControlSystem {}'
HG_CLASS = 'class HG implements VersionControlSystem {'
ABSTRACTBUILDER_CLASS = 'class AbstractBuilder implements Builder {'
PYTESTBUILDER_CLASS = 'class PytestBuilder extends AbstractBuilder {'
JOB_CONFIG = 'class JobConfig {'
COPY_NEXT_LINE = 'COPY NEXT LINE MANUALLY TO POST-BUILD-ACTIONS'
REDMINE_CLASS = 'class Redmine {'


def test_jenkinsdsl__Handler____call____1(tmpdir):
    """It returns a complete groovy dsl template."""
    config_file = tmpdir.join('config.ini')
    config_file.write(r"""
[DEFAULT]
hg_baseurl = https://bitbucket.org
hg_group = gocept

builder = pytest
pytest_timeout = 40
pytest_base_commands =
    \$PYTHON_EXE bootstrap.py
    bin/buildout
pytest_additional_commands =
    bin/test

[gocept.jenkinsdsl]
vcs = hg
builder = pytest
redmine_website_name = gocept
redmine_project_name = gocept.jenkinsdsl
""")
    h = Handler(config_file.open())
    result = h()

    assert result.startswith(CAUTION)
    assert VCS_INTERFACE in result
    assert HG_CLASS in result
    assert ABSTRACTBUILDER_CLASS in result
    assert PYTESTBUILDER_CLASS in result
    assert JOB_CONFIG in result
    assert COPY_NEXT_LINE in result
    assert REDMINE_CLASS in result

    expected_jobconfig = (
        r"new JobConfig(name: 'gocept.jenkinsdsl', "
        r"vcs: new HG(name: 'gocept.jenkinsdsl', "
        r"baseurl: 'https://bitbucket.org', group: 'gocept'), "
        r"builder: new PytestBuilder(timeout: '40', "
        r"base_commands: '\\$PYTHON_EXE bootstrap.py\\nbin/buildout', "
        r"additional_commands: 'bin/test'), "
        r"redmine: new Redmine(website_name: 'gocept', "
        r"project_name: 'gocept.jenkinsdsl'))")
    begin_jobconfig = result.find('new JobConfig')
    result_jobconfig = result[
        begin_jobconfig: begin_jobconfig + len(expected_jobconfig)]
    assert expected_jobconfig == result_jobconfig


def test_jenkinsdsl__Handler____call____2(tmpdir):
    """It does not render specific snippets if there params are not set."""
    config_file = tmpdir.join('config.ini')
    config_file.write(r"""
[gocept.jenkinsdsl]
foo = bar
""")
    result = Handler(config_file.open())()
    assert result.startswith(CAUTION)
    assert VCS_INTERFACE in result
    assert HG_CLASS not in result
    assert ABSTRACTBUILDER_CLASS not in result
    assert PYTESTBUILDER_CLASS not in result
    assert JOB_CONFIG in result
    assert COPY_NEXT_LINE in result
    assert REDMINE_CLASS not in result
