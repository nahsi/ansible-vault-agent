import testinfra.utils.ansible_runner
import pytest
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("dirs", [
    "/opt/vault-agent/",
])
def test_directories_creation(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/opt/vault-agent/vault-agent.json",
])
def test_file_creation(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_file_creation(host):
    f = host.file("/opt/foo")
    assert f.exists
    assert f.is_file
    assert f.contains("bar")


@pytest.mark.parametrize("files", [
    "/opt/vault-agent/template.d/dummy.tmpl",
])
def test_file_sync(host, files):
    f = host.file(files)
    assert not f.exists


@pytest.mark.parametrize("service", [
    "vault-agent"
])
def test_service_is_running(host, service):
    service = host.service(service)

    assert service.is_running
    assert service.is_enabled
