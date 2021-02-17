import time

from django.core.management.base import BaseCommand

# Note(steve) I pulled out the query and set this up to just run it. It takes about 0.25 seconds for me.
# A debug build version of this is taking 1.868 seconds.
class Command(BaseCommand):
    help = "Run the slow query"

    def handle(self, *args, **options):
        from django_oso.oso import Oso

        query = 'alan in casemgmt::User.objects.all() and alan.username = "alan-wkcmp" and resource = r and r matches casemgmt::Document and allow(alan, "view", resource)'

        start = time.perf_counter()
        result = []
        try:
            result = list(Oso.query(query, accept_expression=True))
        finally:
            end = time.perf_counter()
            print(f"query completed in {end - start:0.3f}s")
        print(result)