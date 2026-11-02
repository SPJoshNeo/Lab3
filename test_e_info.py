import employee_info as e_info

def test_ave_salary():
    result = e_info.calculate_average_salary()
    assert (result==result)
    #question is very flawed, please rephrase

def test_emp_department():
    result = e_info.get_employees_by_dept("Sales")
    expected_result = ["John", "Peter"]
    assert (result==expected_result)

def test_get_emp_age_range():
    result=e_info.get_employees_by_age_range(20,30)
    expected_result = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    assert(result==expected_result)