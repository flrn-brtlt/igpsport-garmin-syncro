import requests


class IGPSport:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.token = None

    def login(self):

        url = (
            "https://prod.en.igpsport.com/"
            "service/auth/account/login"
        )

        payload = {
            "appId": "igpsport-web",
            "username": self.username,
            "password": self.password
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        try:
            data = response.json()
        except Exception as e:
            raise Exception(
                f"Keine gültige JSON-Antwort von iGPSPORT "
                f"(HTTP {response.status_code})"
            ) from e

        if data.get("code") != 0:
            raise Exception(
                f"iGPSPORT Login fehlgeschlagen: {data}"
            )

        if "data" not in data:
            raise Exception(
                f"Unerwartete API-Antwort: {data}"
            )

        if "access_token" not in data["data"]:
            raise Exception(
                f"Kein Access Token erhalten: {data}"
            )

        self.token = data["data"]["access_token"]

        print("iGPSPORT Login erfolgreich")

    def get_activities(self):

        url = (
            "https://prod.en.igpsport.com/"
            "service/web-gateway/web-analyze/"
            "activity/queryMyActivity"
            "?pageNo=1&pageSize=10"
            "&reqType=0&sort=1&sortType=1"
        )

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data["data"]["rows"]

    def download_fit(self, ride_id):

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        url = (
            "https://prod.en.igpsport.com/"
            "service/web-gateway/web-analyze/"
            f"activity/getDownloadUrl/{ride_id}"
        )

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        download_url = response.json()["data"]

        fit_file = requests.get(
            download_url,
            timeout=60
        )

        fit_file.raise_for_status()

        filename = f"downloads/{ride_id}.fit"

        with open(filename, "wb") as f:
            f.write(fit_file.content)

        return filename
