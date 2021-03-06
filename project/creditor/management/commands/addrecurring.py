from django.core.management.base import BaseCommand, CommandError
from creditor.models import RecurringTransaction

class Command(BaseCommand):
    help = 'Gets all RecurringTransactions and runs conditional_add_transaction()'

    def handle(self, *args, **options):
        for t in RecurringTransaction.objects.all():
            ret = t.conditional_add_transaction()
            if ret:
                print("Created transaction %s" % ret)
