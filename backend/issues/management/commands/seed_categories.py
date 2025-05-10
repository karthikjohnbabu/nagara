from django.core.management.base import BaseCommand
from issues.models import IssueCategory

class Command(BaseCommand):
    help = "Seed initial civic issue categories (Tier 1, 2, 3)"

    def handle(self, *args, **kwargs):
        categories = [
            # Tier 1
            "Water Supply",
            "Drainage & Sewage",
            "Waste Management",
            "Electricity",
            "Roads & Potholes",
            "Gas Line",

            # Tier 2
            "Street Lights",
            "Public Toilets",
            "Encroachments",
            "Noise Pollution",
            "Tree Cutting / Greenery",
            "Construction Hazards",
            "Stray Animals",

            # Tier 3
            "Suggestions",
            "Other / Misc",
            "Volunteer Calls",
        ]

        for name in categories:
            category, created = IssueCategory.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Added: {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Already exists: {name}"))
