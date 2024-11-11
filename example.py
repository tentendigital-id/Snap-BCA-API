from snap_bca_api.bca import BCA_SNAP

host = 'https://sandbox.bca.co.id'
client_id = 'your client_id'
client_secret = 'your client_secret'
private_key = "-----BEGIN PRIVATE KEY-----\nYour private key without space\n-----END PRIVATE KEY-----"  # noqa
channel_id = "your channel_id"
partner_id = "Your partner_id"
account_number = "Your bank account number"

bca = BCA_SNAP(
    client_id=client_id,
    client_secret=client_secret,
    private_key=private_key,
    channel_id=channel_id,
    partner_id=partner_id,
    host=host,
    debug=True
)

get_balance = bca.getBalance(
    account_number=account_number,
    partnerReferenceNo="12345"
)
print(get_balance)


get_statement = bca.getStatement(
    account_number=account_number,
    partnerReferenceNo="12345",
    fromDateTime="2024-10-29T00:00:00+07:00",
    toDateTime="2024-11-11T00:00:00+07:00"
)
print(get_statement)
