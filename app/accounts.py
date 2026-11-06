
# Penyimpanan akun sementara
accounts = []

# Membuat akun baru
def create_account(name: str, email: str):
    account = {
        "id": len(accounts) + 1,
        "name": name,
        "email": email,
        "balance": 0
    }

    accounts.append(account)

    return account


# Mengambil seluruh akun
def get_all_accounts():
    return accounts
