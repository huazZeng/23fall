import requests
class onlinesearch:
    def __init__(self):
        self.url = 'http://120.46.222.41:5000/map/data'  
    def operation_1(self,A,B):
        data = {'operation': '1', 'location1': A,'location2':B}

        response = requests.post(self.url, data=data)
        return response.text
        # 打印响应的状态码和内容
        # print(f'Status Code: {response.status_code}')
        # print('Response Content:')
        # print(response.text)
    def operation_2(self,A):
        data = {'operation': '2', 'location1': A,'location2':A}

        response = requests.post(self.url, data=data)
        return response.text

    def operation_3(self):
        data = {'operation': '3', 'location1': '','location2':''}

        response = requests.post(self.url, data=data)
        return response.text

    def operation_4(self,A):
        data = {'operation': '4', 'location1': A,'location2':''}

        response = requests.post(self.url, data=data)
        return response.text