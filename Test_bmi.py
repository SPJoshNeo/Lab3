import Lab2.bmi as bmi

def test_bmi_normal_weight():
    expected_result = 0
    result = bmi.calculate_bmi(1.0,19.0)
    assert(result==expected_result)

def test_bmi_over_weight():
    expected_result = 1
    result = bmi.calculate_bmi(1.0,30.0)
    assert (result == expected_result)



def test_bmi_under_weight():
    expected_result = -1
    result = bmi.calculate_bmi(1.0,18.0)
    assert (result == expected_result)