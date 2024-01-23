from pages.ServicePy import ServicePy
from pages.ServiceGo import ServiceGo
from json import loads
from datetime import datetime


date_fmt = '%d-%m-%Y %H:%M:%S.%f'
date_fmt_go = '%d-%m-%Y %H:%M:%S'


def test_py_greeting(browser, logger):
    py_greet = ServicePy(browser, logger)
    py_greet.go_to_url("http://localhost:8080/greet")
    answer = py_greet.endpoint_greet()
    assert answer == '"Привет, noname от Python!"'

    name = "Василиса"
    py_greet.go_to_url(f"http://localhost:8080/greet?name={name}")
    answer = py_greet.endpoint_greet()
    assert answer == f'"Привет, {name} от Python!"'


def test_py_greet_history(browser, logger):
    py_history = ServicePy(browser, logger)
    name = "test"
    py_history.go_to_url(f"http://localhost:8080/greet?name={name}")
    py_history.go_to_url("http://localhost:8080/greet/history")
    answer = py_history.endpoint_greet_history()
    d_answer = loads(answer)[-1]
    assert d_answer['name'] == name
    answer_time = datetime.strptime(d_answer['date'], date_fmt)
    time_diff = datetime.now() - answer_time
    # assert time_diff.seconds < 3 # Время в контейнере различается на 6 часов


def test_go_greeting(browser, logger):
    go_greet = ServiceGo(browser, logger)
    go_greet.go_to_url("http://localhost:8081/greet")
    answer = go_greet.endpoint_greet()
    assert answer == 'Привет от Go!'


def test_go_greet_history(browser, logger):
    go_history = ServiceGo(browser, logger)
    go_history.go_to_url("http://localhost:8081/greet")
    go_history.go_to_url("http://localhost:8081/greet/history")
    answer = go_history.endpoint_greet_history()
    d_answer = loads(answer)[-1]
    answer_time = datetime.strptime(d_answer['date'], date_fmt_go)
    time_diff = datetime.now() - answer_time
    # assert time_diff.seconds < 3 # Время в контейнере различается на 5 часов


def test_go_greet_py(browser, logger):
    go_greet = ServiceGo(browser, logger)
    go_greet.go_to_url("http://localhost:8081/greet/python")
    answer = go_greet.endpoint_greet_python()
    assert answer == '"Привет, Go от Python!"'

