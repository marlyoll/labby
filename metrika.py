import requests

class YandexMetrikaAPI:
    def init(self, token):
        self.token = token
        self.base_url = "https://api-metrika.yandex.net/stat/v1/data"
        self.headers = {
            "Authorization": f"OAuth {self.token}"
        }

    def get_metrics(self, counter_id, metrics):
        params = {
            "id": counter_id,
            "metrics": metrics,
            "date1": "2025-04-01",
            "date2": "2025-04-12"
        }
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

# Использование
token = y0__xDUy6v_BhiC-jYgi6a75xJW4hmIcBNWtS76ECSaNM1E4u2iyg
counter_id = 101037628
metrics = "ym:s:visits,ym:s:pageviews,ym:s:users"

api = YandexMetrikaAPI(token)
data = api.get_metrics(counter_id, metrics)
print(data)
