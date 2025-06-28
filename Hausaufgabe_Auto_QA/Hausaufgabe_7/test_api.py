from hausaufgabe_7 import EmployeeApi
from dict_param import CREATE_EMPLOYEE,UPDATE_EMPLOYEE

def test_create_employee():

    base_url = "http://5.101.50.27:8000"
    api = EmployeeApi(base_url)
    employee_id = api.create_employee(**CREATE_EMPLOYEE)
    api.get_info_employee(employee_id)
    update = api.update_employee(employee_id,**UPDATE_EMPLOYEE)
    print(update)



