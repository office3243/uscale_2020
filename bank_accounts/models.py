from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from decimal import Decimal
from django.db.models import Sum
from django.db.models.signals import post_save, pre_save


class BankAccount(models.Model):
    party = models.ForeignKey("parties.Party", on_delete=models.CASCADE)
    account_code = models.CharField(max_length=7, unique=True)
    amount_limit = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal(1000000), editable=False)
    account_holder = models.CharField(max_length=128)
    acc_no = models.CharField(max_length=32)
    ifsc_code = models.CharField(max_length=11, validators=[MinLengthValidator(limit_value=11)])
    bank_name = models.CharField(max_length=64)
    branch_name = models.CharField(max_length=64, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {} - {}".format(self.party.name, self.bank_name, self.acc_no[-5:])

    @property
    def get_display_text(self):
        return "{} - {} - {}".format(self.account_holder, self.bank_name, self.acc_no[-5:])

    @property
    def get_tr_amount(self):
        return self.accounttransaction_set.aggregate(total=Sum("amount"))['total']

    @property
    def generate_account_code(self):
        all_accounts = self.party.bankaccount_set.all().order_by("id")
        ac_index = list(all_accounts).index(self)
        return self.party.party_code + chr(ac_index+65)


def assign_account_code(sender, instance, *args, **kwargs):
    print("post save")
    account_code = instance.generate_account_code
    if instance.account_code != account_code:
        instance.account_code = account_code
        instance.save()


post_save.connect(assign_account_code, sender=BankAccount)
