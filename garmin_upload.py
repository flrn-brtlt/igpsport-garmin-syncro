from garminconnect import Garmin


class GarminUploader:

    def __init__(self, email, password):

        self.client = Garmin(
            email,
            password
        )

        self.client.login()

    def upload(self, fit_file):

        try:

            self.client.upload_activity(
                fit_file
            )

            print(
                f"Hochgeladen: {fit_file}"
            )

        except Exception as e:

            if "Duplicate" in str(e):

                print(
                    "Aktivität bereits vorhanden"
                )

            else:
                raise e