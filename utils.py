import requests
url = "http://127.0.0.1:8000/create_problem/1/"
data = {
    "name": "masala",
    "problem": "asdsaijd asoi jasoi jdasoi jdoasij asoij doas ijdasojid oasijd asdsaijd asoi jasoi jdasoi jdoasij asoij doas ijdasojid oasijdasdsaijd asoi jasoi jdasoi jdoasij asoij doas ijdasojid oasijdasdsaijd asoi jasoi jdasoi jdoasij asoij doas ijdasojid oasijdasdsaijd asoi jasoi jdasoi jdoasij asoij doas ijdasojid oasijdasdsaijd asoi jasoi jdasoi jdoasij asoij doas ijdasojid oasijdasdsaijd asoi jasoi jdasoi jdoasij asoij doas ijdasojid oasijdasdsaijd asoi jasoi jdasoi jdoasij asoij doas ijdasojid oasijd",
    "comment": "https://www.google.com",
    "infoin": "asd",
    "infoout": "asds",
    "simpletests": "{'1': '1'}",
    "tests": '{"2": "2"}'
}
res = requests.post(url, data)
print(res.text)