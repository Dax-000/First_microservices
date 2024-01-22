from pages.ServicePy import ServicePy


def test_greeting(browser, logger):
    py_greet = ServicePy(browser, logger)
    py_greet.go_to_url("http://localhost:8080/greet")
    answer = py_greet.endpoint_greet()
    assert answer == '"Привет, None от Python!"'

    name = "Василиса"
    py_greet.go_to_url(f"http://localhost:8080/greet?name={name}")
    answer = py_greet.endpoint_greet()
    assert answer == f'"Привет, {name} от Python!"'
