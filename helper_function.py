import requests
import setting

def load_temple(input_file):
    """Load template"""
    url = setting.DOMEN_NAME + '/api/v1/templates'
    file = {
        'file': open(f'test_files/{input_file}', 'rb')
    }
    r = requests.put(url, files=file)
    assert r.status_code == 201, 'загрузка тестового шаблона неуспешна'

def get_first_tamplate():
    url = setting.DOMEN_NAME + '/api/v1/templates'
    r = requests.get(url)
    list_templates=r.json()['templates']
    print(list_templates)
    assert r.status_code == 200 and len(list_templates)>0, 'Нет шаблонов в списке'
    return list_templates[0]
