import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = "Import phones from phones.csv"

    def handle(self, *args, **options):

        csv_path = "phones.csv"

        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:

                row.pop("", None)

                Phone.objects.update_or_create(
                    id=int(row["id"]),
                    defaults={
                        "name": row["name"],
                        "price": int(row["price"]),
                        "image": row["image"],
                        "release_date": row["release_date"],
                        "lte_exists": row["lte_exists"].strip().lower() == "true",
                    },
                )

        self.stdout.write(self.style.SUCCESS("Phones imported successfully"))
