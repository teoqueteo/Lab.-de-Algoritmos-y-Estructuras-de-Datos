from city_module.city_functions_1 import city_country

def test_city_country():
    resultado = city_country('santiago', 'chile')
    assert resultado == 'Santiago, Chile'