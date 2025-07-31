import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

KEY_DIR = "keys"
os.makedirs(KEY_DIR, exist_ok=True)

def generate_keys(username):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    with open(f"{KEY_DIR}/{username}_private.pem", "wb") as f:
        f.write(private_key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption()
        ))

    with open(f"{KEY_DIR}/{username}_public.pem", "wb") as f:
        f.write(public_key.public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def sign_data(username, data):
    with open(f"{KEY_DIR}/{username}_private.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
    return private_key.sign(data.encode(), padding.PKCS1v15(), hashes.SHA256()).hex()

def verify_signature(username, data, signature_hex):
    with open(f"{KEY_DIR}/{username}_public.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())
    try:
        public_key.verify(bytes.fromhex(signature_hex), data.encode(), padding.PKCS1v15(), hashes.SHA256())
        return True
    except:
        return False