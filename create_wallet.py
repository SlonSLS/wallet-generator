from solders.keypair import Keypair
import base58

# Generate a new keypair
keypair = Keypair()

# Get the public key (wallet address)
public_key = keypair.pubkey()

# Get the secret key (private key)
secret_key = keypair.secret()

print("Public Key (Wallet Address):", public_key)
print("Secret Key (Private Key):", secret_key)

# Save secret key to a file
with open('secret_key.txt', 'w') as f:
    f.write(base58.b58encode(secret_key).decode('utf-8'))

# Save public key to a file
with open('public_key.txt', 'w') as f:
    f.write(str(public_key))
