import setting
import requests
import pytest
import helper_function


def test_get_method():
    """Check GET method - get template list"""
    url = setting.DOMEN_NAME + '/api/v1/templates'
    r = requests.get(url)
    assert r.status_code == 200 and 'templates' in r.json(), f"Неверный код ответа: {r.status_code}"


@pytest.mark.parametrize(
    "input_file,code",
    [
        ('good_file2.yaml', 201),
        ('bad_file.file', 400),
        ('bad_file.txt', 400)
    ]
)
def test_put_method_files(input_file, code):
    """Check PUT method - load different file format of template"""
    url = setting.DOMEN_NAME + '/api/v1/templates'
    data = {}
    file = {
        'file': open(f'test_files/{input_file}', 'rb')
    }
    r = requests.put(url, data=data, files=file)
    assert r.status_code == code, f"Неверный код ответа: {r.status_code},message: {r.content} "


@pytest.mark.parametrize(
    "data,code,input_file",
    [
        ({"tmpl_id": "my_custom_id"}, 201, 'good_file.yaml'),
        ({}, 201, 'good_file.yaml'),
        ({"tmpl_id": "qwe2134wqr"}, 201, 'good_file.yaml'),
        ({"asdfewfewv": "qwe2134wqr"}, 201, 'good_file.yaml'),
        ({"": "qwe2134wqr"}, 201, 'good_file.yaml')
    ]
)
def test_put_different_data(data, code, input_file):
    """Check PUT method - load template with different data in body requests"""
    url = setting.DOMEN_NAME + '/api/v1/templates'
    data = data
    file = {
        'file': open(f'test_files/{input_file}', 'rb')
    }
    r = requests.put(url, data=data, files=file)
    assert r.status_code == code, f"Неверный код ответа: {r.status_code},message: {r.content} "

@pytest.mark.parametrize(
    "input_file,code,what_check",
    [
        ('good_file.yaml', 200,'id and label is set'),
        ('good_file2.yaml', 200,'id,label,link, depends is set'),
        ('good_file3.yaml', 200,'id,label,link'),
        ('bad_file.yaml', 500,'id and label not is set'),
        ('bad_file2.yaml', 500,'id and link is set, label not is set'),
        ('bad_file3.yaml', 500,'label and depends is set, id and link not is set')
    ]
)
def test_content_template_yaml_file(input_file,code,what_check):
    """Check POST method - try install template with different data inside yaml-file """
    print(f'here need add to allure.step or allure.attach description: {what_check}')
    helper_function.load_temple(input_file)
    url = setting.DOMEN_NAME + f'/api/v1/templates/{input_file.split(".")[0]}/install'
    r = requests.post(url)
    assert r.status_code == code, f"Неверный код ответа: {r.status_code},message: {r.content} "

@pytest.mark.parametrize(
    "input_file,code",
    [
        ('good_file.yaml', 200),
        ('good_file_same_id.yaml', 400),
    ]
)
def test_Id_should_be_unique(input_file, code):
    """Check unique id between different tamplate"""
    helper_function.load_temple(input_file)
    url = setting.DOMEN_NAME + f'/api/v1/templates/{input_file.split(".")[0]}/install'
    r = requests.post(url)
    assert r.status_code == code, f"Неверный код ответа: {r.status_code},message: {r.content} "


def test_post_method():
    """Check POST method - install template"""
    helper_function.load_temple('good_file.yaml')
    first_template = helper_function.get_first_tamplate()
    url = setting.DOMEN_NAME + f'/api/v1/templates/{first_template}/install'
    r = requests.post(url)
    assert r.status_code == 200, f"Неверный код ответа: {r.status_code}"


def test_delete_method():
    """check DELETE method - delete template"""
    helper_function.load_temple('delete_file.yaml')
    url = setting.DOMEN_NAME + '/api/v1/templates/delete_file'
    r = requests.delete(url)
    assert r.status_code == 200, f"Неверный код ответа: {r.status_code}"
