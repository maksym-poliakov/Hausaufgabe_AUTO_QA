import requests

class  EmployeeApi:

    def __init__(self,url):
        self.url = url

    def create_employee_empty_body(self):

        resp = requests.post(self.url + '/employee/create',json={})
        response = resp.json()
        print(response)
        assert resp.status_code == 422, f"Ожидался 422, получен {resp.status_code}"

    def create_employee(self, **kwargs):

        resp = requests.post(f"{self.url}/employee/create", json=kwargs)

        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        assert resp.json()["first_name"] == kwargs["first_name"],f"Ошибка: ожидался {kwargs["first_name"]} получен {resp.json()["first_name"]}"
        assert resp.json()["last_name"] == kwargs["last_name"],f"Ошибка: ожидался {kwargs["last_name"]} получен {resp.json()["last_name"]}"
        assert resp.json()["middle_name"] == kwargs["middle_name"], f"Ошибка: ожидался {kwargs["middle_name"]} получен {resp.json()["middle_name"]}"
        assert resp.json()["company_id"] == kwargs["company_id"], f"Ошибка: ожидался {kwargs["company_id"]} получен {resp.json()["company_id"]}"
        assert resp.json()["email"] == kwargs["email"], f"Ошибка: ожидался {kwargs["email"]} получен {resp.json()["email"]}"
        assert resp.json()["phone"] == kwargs["phone"], f"Ошибка: ожидался {kwargs["phone"]} получен {resp.json()["phone"]}"
        assert resp.json()["birthdate"] == kwargs["birthdate"], f"Ошибка: ожидался {kwargs["birthdate"]} получен {resp.json()["birthdate"]}"

        return resp.json()['id']

    def get_info_employee(self,employee_id):
        resp = requests.get(f"{self.url}/employee/info/{employee_id}")
        assert resp.status_code == 200,f"Ошибка: Сотрудник с employee_id {employee_id} не найден"
        return resp.json()

    def get_list_employee(self,company_id):
        resp = requests.get(f"{self.url}/employee/list/{company_id}")
        assert resp.status_code == 200 ,f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_token(self):
        creds = {"username": "harrypotter", "password": "expelliarmus"}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]

    def update_employee(self,employee_id,**kwargs):

        token = self.get_token()
        resp = requests.patch(self.url + f'/employee/change/{employee_id}?client_token={token}', json=kwargs )
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        assert resp.json()["id"] == employee_id, f"Ошибка: ожидался ID: {employee_id} получен {resp.json()["id"]}"
        assert resp.json()["last_name"] == kwargs["last_name"] , f"Ошибка: ожидался {kwargs["last_name"]} получен {resp.json()["last_name"]}"
        assert resp.json()["email"] == kwargs["email"], f"Ошибка: ожидался {kwargs["email"]} получен {resp.json()["email"]}"
        assert resp.json()["phone"] == kwargs["phone"], f"Ошибка: ожидался {kwargs["phone"]} получен {resp.json()["phone"]}"
        assert resp.json()["is_active"] == kwargs["is_active"], f"Ошибка: ожидался {kwargs["is_active"]} получен {resp.json()["is_active"]}"
        return resp.json()



