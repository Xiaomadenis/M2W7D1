import secrets
import string
from typing import Literal


_sysrand = secrets.SystemRandom()


AMBIGUI = set("Il1O0o")

def _remove_ambiguous(s: str) -> str:
    return "".join(ch for ch in s if ch not in AMBIGUI)

def generate_password(
    mode: Literal["simple", "complex"] = "simple",
    length: int | None = None,
    avoid_ambiguous: bool = False,
) -> str:
    """
    Genera una password sicura.
    - mode="simple": alfanumerica (default len=8)
    - mode="complex": ASCII stampabili (default len=20) con almeno:
      1 minuscola, 1 maiuscola, 1 cifra, 1 simbolo
    - avoid_ambiguous=True per escludere caratteri come O/0, I/l/1, o
    """
    if mode == "simple":
        charset = string.ascii_letters + string.digits
        L = 8 if length is None else length
        if avoid_ambiguous:
            charset = _remove_ambiguous(charset)
        if L <= 0:
            raise ValueError("La lunghezza deve essere > 0")
        return "".join(secrets.choice(charset) for _ in range(L))

    elif mode == "complex":
        L = 20 if length is None else length
        if L < 4:
            raise ValueError("La modalità 'complex' richiede almeno 4 caratteri")

        lowers  = string.ascii_lowercase
        uppers  = string.ascii_uppercase
        digits  = string.digits
        symbols = string.punctuation  

        if avoid_ambiguous:
            lowers = _remove_ambiguous(lowers)
            uppers = _remove_ambiguous(uppers)
            digits = _remove_ambiguous(digits)

        all_chars = lowers + uppers + digits + symbols

        
        pwd_chars = [
            secrets.choice(lowers),
            secrets.choice(uppers),
            secrets.choice(digits),
            secrets.choice(symbols),
        ]
        
        pwd_chars += [secrets.choice(all_chars) for _ in range(L - len(pwd_chars))]
    
        _sysrand.shuffle(pwd_chars)
        return "".join(pwd_chars)

    else:
        raise ValueError("mode deve essere 'simple' o 'complex'")

if __name__ == "__main__":
    ans = input("Password semplice o complessa? S/C ").strip().upper()
    mode = "complex" if ans == "C" else "simple"

    raw_len = input("Lunghezza (invio = default 8/20): ").strip()
    if raw_len:
        try:
            length = int(raw_len)
        except ValueError:
            print("Lunghezza non valida, uso il default.")
            length = None
    else:
        length = None

    avoid = input("Escludere caratteri ambigui (O/0, I/l/1)? y/N ").strip().lower() == "y"

    print("Password:", generate_password(mode, length, avoid))
