from __future__ import annotations

from ..helpers import make_client


def test_api_files_module_surface() -> None:
    client, _ = make_client()
    module = client.api.files
    assert callable(module.delete_file_api)
    assert callable(module.list_files)
    assert callable(module.delete_many_files_api)
    assert callable(module.commit_upload)
    assert callable(module.download_file_api)
    assert callable(module.get_file_info)
    assert callable(module.get_signed_url)
    assert callable(module.request_upload_url)


def test_api_files_delete_file_api_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.files.delete_file_api(files_integration_id="stub-files_integration_id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_api_files_list_files_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.files.list_files(files_integration_id="stub-files_integration_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_api_files_delete_many_files_api_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.files.delete_many_files_api(files_integration_id="stub-files_integration_id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_api_files_commit_upload_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.files.commit_upload(files_integration_id="stub-files_integration_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_api_files_download_file_api_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.files.download_file_api(files_integration_id="stub-files_integration_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_api_files_get_file_info_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.files.get_file_info(files_integration_id="stub-files_integration_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_api_files_get_signed_url_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.files.get_signed_url(files_integration_id="stub-files_integration_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_api_files_request_upload_url_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.files.request_upload_url(files_integration_id="stub-files_integration_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
