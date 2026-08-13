#!/usr/bin/env python3
import re, sys
from pathlib import Path

def validate(text):
    issues = []
    headings = re.findall(r'(?m)^\s*(\d+(?:\.\d+)?)\s*[-–.]?\s+(.+)$', text)
    top = [h for h in headings if "." not in h[0]]
    seen = {}
    for num, title in top:
        if num in seen:
            issues.append(f"Numeração principal duplicada: {num} ({seen[num]} / {title})")
        seen[num] = title
    placeholders = re.findall(r'\[(?:INFORMAR|FATO GERADOR|VALOR|[A-ZÁÉÍÓÚÇ _-]{3,})\]', text)
    if placeholders:
        issues.append("Placeholders pendentes: " + ", ".join(sorted(set(placeholders))))
    if "DANO MORAL" in text.upper() or "DANOS EXTRAPATRIMONIAIS" in text.upper():
        anchor = "Com o advento da Lei 13.467/2017"
        if anchor not in text:
            issues.append("Há dano moral/extrapatrimonial sem a matriz obrigatória.")
    for s in ["contrato do contrato", "faz a jus"]:
        if s.lower() in text.lower():
            issues.append(f"Expressão suspeita: {s}")
    return issues

def main():
    if len(sys.argv) != 2:
        print("Uso: python validate_petition.py arquivo.md")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    issues = validate(text)
    if issues:
        print("VALIDAÇÃO: ATENÇÃO")
        for i in issues:
            print("-", i)
        raise SystemExit(1)
    print("VALIDAÇÃO: OK")

if __name__ == "__main__":
    main()
