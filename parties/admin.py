from django.contrib import admin
from .models import Party, Wallet, WalletAdvance
from import_export.admin import ImportExportModelAdmin


def get_party_name(instance):
    return instance.party.name


class PartyAdmin(ImportExportModelAdmin):

    list_display = ("party_code", "name", "phone", "email", "is_wallet_party")


class WalletAdmin(admin.ModelAdmin):

    list_display = (get_party_name, "balance", "deduct_type", "fixed_amount", "is_active")


class WalletAdvanceAdmin(admin.ModelAdmin):
    pass
    #
    # list_display = ("wallet", "amount", "payed_on", "p_2")
    # list_filter = ("wallet", "amount", "payed_on")
    # list_editable = ("payed_on", )


admin.site.register(Party, PartyAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(WalletAdvance, WalletAdvanceAdmin)

