from typing import List

def lunghezze_parole(A: List[str]) -> List[int]:
    return [len(parola) for parola in A]

if __name__ == "__main__":
    A = ["scrivo", "questa", "lista", "di", "parole"]
    B = lunghezze_parole(A)
    print("Input A:", A)
    print("Output B:", B)