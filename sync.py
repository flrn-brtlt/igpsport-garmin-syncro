import os

from database import *
from igpsport import IGPSport
from garmin_upload import GarminUploader


create_db()

os.makedirs(
    "downloads",
    exist_ok=True
)

config = {
    "igpsport_username": os.environ["IGPSPORT_USER"],
    "igpsport_password": os.environ["IGPSPORT_PASSWORD"],
    "garmin_email": os.environ["GARMIN_USER"],
    "garmin_password": os.environ["GARMIN_PASSWORD"]
}


def sync():

    print(
        "\nNeue Synchronisation startet..."
    )

    igps = IGPSport(
        config["igpsport_username"],
        config["igpsport_password"]
    )

    igps.login()

    activities = igps.get_activities()

    print(
        f"{len(activities)} Aktivitäten gefunden"
    )

    garmin = None

    for activity in activities:

        ride_id = activity["rideId"]

        print(
            f"Prüfe Fahrt {ride_id}"
        )

        if already_synced(ride_id):
            print(
                f"Bereits synchronisiert: {ride_id}"
            )
            continue

        print(
            f"Neue Fahrt gefunden: {ride_id}"
        )

        if garmin is None:

            print(
                "Verbinde zu Garmin..."
            )

            garmin = GarminUploader(
                config["garmin_email"],
                config["garmin_password"]
            )

            print(
                "Garmin Login erfolgreich"
            )

        fit_file = igps.download_fit(
            ride_id
        )

        garmin.upload(
            fit_file
        )

        mark_synced(
            ride_id
        )

        print(
            f"Fahrt {ride_id} synchronisiert"
        )


sync()
