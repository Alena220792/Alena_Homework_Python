import requests

class YouGileApi:
    def __init__(self, url: str):
        self.url = url

    # [POST] Создание проекта
    def create_project(self, token: str, name: str):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
                   
        body = {
            "title": name
        }
        resp = requests.post(f"{self.url}projects", json=body, headers=headers)
        return resp

    # [PUT] Обновление проекта
    def update_project(self, token: str, project_id: int, new_name: str):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        body = {
            "title": new_name
        }
        resp = requests.put(f"{self.url}projects/{project_id}", json=body, headers=headers)
        return resp
    
    
    # [GET] Получение проекта
    def get_project(self, token: str, project_id: int):
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(f"{self.url}projects/{project_id}", headers=headers)
        return resp

    # [DELETE] Удаление проекта
    def delete_project(self, token, project_id):
        """
        Метод для удаления проекта по его ID.
        """
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}projects/{project_id}"
        
        response = requests.delete(url, headers=headers)
        return response