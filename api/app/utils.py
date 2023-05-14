from typing import Union
from cryptography.fernet import Fernet
from pathlib import Path

FERNET_KEY_FILE_PATH = "fernet_key.key"


def generating_fernet_key() -> Union[bytes, str]:
    return Fernet.generate_key()


def dumping_fernet_key_into_file(fernet_key: Union[bytes, str]):
    # set file permissions to read and write only for the owner
    with open(FERNET_KEY_FILE_PATH, "wb") as f:
        f.write(fernet_key)
    Path(FERNET_KEY_FILE_PATH).chmod(0o600)


def load_fernet_key_from_file() -> Union[bytes, str]:
    with open(FERNET_KEY_FILE_PATH, "rb") as f:
        key = f.read()
    return Fernet(key)


def encrypt_private_key(private_key: str) -> bytes:
    fernet_key = load_fernet_key_from_file()
    return fernet_key.encrypt(private_key.encode())


def decrypt_private_key(encrypted_key: bytes) -> str:
    fernet_key = load_fernet_key_from_file()
    return fernet_key.decrypt(encrypted_key).decode()
