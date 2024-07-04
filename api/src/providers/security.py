from pwdlib import PasswordHash


pwd = PasswordHash.recommended()

def password_hash(password: str) -> str:
    """Generate a hash from string"""
    return pwd.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """Check if passwords are equal"""
    return pwd.verify(password, hashed_password)
