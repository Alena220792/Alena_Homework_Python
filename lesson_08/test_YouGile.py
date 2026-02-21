import pytest
from .YouGileApi import YouGileApi

# вставить токен для работы тестов
auth_token = "IyFvHLg8NPVNyav86XMPYBVOMGtCsR9HtWcHc8jLp8DHr239LAvUsx3WcZbLXqUG"
base_url = "https://ru.yougile.com/api-v2/"

api = YouGileApi(base_url)

# ПОЗИТИВНЫЕ ТЕСТЫ

@pytest.mark.positive
def test_create_project_positive():
    name = "Домашка08"
    resp = api.create_project(auth_token, name)
    assert resp.status_code == 201
    project_data = resp.json()
    assert "id" in project_data

    project_data = resp.json()
    assert "id" in project_data

    try:
        delete_resp = api.delete_project(auth_token, project_data["id"])
        assert delete_resp.status_code == 204, f"Не удалось удалить проект {project_data['id']}"
    except Exception as e:
        print(f"Предупреждение: не удалось очистить проект {project_data.get('id', 'unknown')}: {e}")
    
  
@pytest.mark.positive
def test_update_project_positive():
    created = api.create_project(auth_token, "Новый проект").json()
    p_id = created["id"]
    new_name = "Новая домашка 08"
    
    resp_update = api.update_project(auth_token, p_id, new_name)
    assert resp_update.status_code == 200
    assert "id" in resp_update.json()

    resp_get = api.get_project(auth_token, p_id)
    assert resp_get.status_code == 200
    assert resp_get.json()["title"] == new_name
    
    try:
        delete_resp = api.delete_project(auth_token, p_id)
        assert delete_resp.status_code == 204, f"Не удалось удалить проект {p_id}"
    except Exception as e:
        print(f"Предупреждение: не удалось очистить проект {p_id}: {e}")

@pytest.mark.positive
def test_get_project_positive():
    created = api.create_project(auth_token, "Вновь созданный проект для получения").json()
    p_id = created["id"]
    
    resp = api.get_project(auth_token, p_id)
    assert resp.status_code == 200
    assert resp.json()["id"] == p_id
 
    try:
        delete_resp = api.delete_project(auth_token, p_id)
        assert delete_resp.status_code == 204, f"Не удалось удалить проект {p_id}"
    except Exception as e:
        print(f"Предупреждение: не удалось очистить проект {p_id}: {e}")


# НЕГАТИВНЫЕ ТЕСТЫ

@pytest.mark.negative
def test_create_project_without_title_negative():
    resp = api.create_project(auth_token, "")
    assert resp.status_code == 400

@pytest.mark.negative
def test_update_project_invalid_token_negative():
    bad_token = "token_123"
    resp = api.update_project(bad_token, 1, "проект для ошибки")
    assert resp.status_code == 401
  
@pytest.mark.negative
def test_get_non_existent_project_negative():
    invalid_id = 99999999
    resp = api.get_project(auth_token, invalid_id)
    assert resp.status_code == 404