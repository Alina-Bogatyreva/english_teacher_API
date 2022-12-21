import requests


domain = "http://127.0.0.1:8000"
# r = requests.request("GET", f"{domain}/word/guess")
# print(r.status_code)
# print(r.json())

# r = requests.request("POST", f"{domain}/word/check", json={'question_id': 1001, 'answer': "апельсин"})
# print(r.json())

# r = requests.request('GET', domain+"/word/result/1001")
# print(r.status_code)
# print(r.json())

# r = requests.request("GET", f"{domain}/letter/guess")
# print(r.status_code)
# print(r.json())

# r = requests.request("POST", f"{domain}/letter/check", json={'question_id': 1002, "skip_letter": "p"})
# print(r.json())

r = requests.request('GET', domain+"/letter/result/1002")
print(r.status_code)
print(r.json())