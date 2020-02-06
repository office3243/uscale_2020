from django.contrib import admin
from .models import BankAccount
from import_export.admin import ImportExportModelAdmin


class BankAccountAdmin(ImportExportModelAdmin):

    list_display = ("party", "account_code", "acc_no", "ifsc_code", "bank_name", "branch_name")
    list_filter = ("party", "bank_name")


admin.site.register(BankAccount, BankAccountAdmin)
