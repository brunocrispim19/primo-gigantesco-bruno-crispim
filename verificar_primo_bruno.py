#!/usr/bin/env python3
"""
Auditoria e Verificação Determinística Independente
Primo Gigantesco de Bruno de Paula Crispim (10.111 Dígitos)
Teorema de Proth (1878) & Reciprocidade Quadrática de Gauss
"""

import time
import hashlib
import sys
sys.set_int_max_str_digits(25000)

def verify():
    print("=" * 75)
    print("VERIFICAÇÃO DETERMINÍSTICA DO PRIMO DE BRUNO DE PAULA CRISPIM")
    print("=" * 75)
    
    # 1. Verificar ancoragem na semente SHA-256
    seed = "bruno de paula crispim"
    seed_hash = hashlib.sha256(seed.encode('utf-8')).hexdigest()
    print(f"[*] Semente textual: '{seed}'")
    print(f"[*] Hash SHA-256 da semente: {seed_hash}")
    expected_seed_hash = "2a01a475c1a0032d83686140d70c158bf6a77b47a071998eb9ea82173b0fa061"
    assert seed_hash == expected_seed_hash, "Erro na ancoragem da semente!"
    print("    [OK] Ancoragem criptográfica verificada com sucesso.")
    
    # 2. Parâmetros de Proth
    n = 33334
    k = 19000041548667697985925397706689617339423511024733994245427679492849705940689
    print(f"[*] Expoente n = {n} (par, garantindo 2^n = 1 mod 3)")
    print(f"[*] Multiplicador k = {k} (k = 1 mod 6, k < 2^n)")
    
    assert k < (1 << n), "Condição k < 2^n falhou!"
    assert k % 2 == 1, "k deve ser ímpar!"
    assert k % 3 == 1, "k mod 3 deve ser 1!"
    print("    [OK] Premissas de Proth e Reciprocidade Quadrática satisfeitas.")
    
    # 3. Construção aritmética exata
    print("[*] Reconstruindo P = k * 2^n + 1...")
    t0 = time.time()
    P = (k << n) + 1
    t_reconstruct = time.time() - t0
    
    s_digits = str(P)
    num_digits = len(s_digits)
    bit_len = P.bit_length()
    print(f"    [OK] Reconstruído em {t_reconstruct:.4f}s.")
    print(f"[*] Total de dígitos decimais: {num_digits}")
    print(f"[*] Comprimento binário: {bit_len} bits")
    assert num_digits == 10111, f"Esperado 10111 dígitos, obtido {num_digits}"
    
    # 4. Hash SHA-256 dos dígitos decimais
    h_p = hashlib.sha256(s_digits.encode('utf-8')).hexdigest()
    print(f"[*] SHA-256 dos 10.111 dígitos: {h_p}")
    assert h_p == "b076332f5e4bd7d252bde6b8bed0079c5286628ad96766287ffa2b7c661f5817", "Hash de integridade divergente!"
    print("    [OK] Integridade digital dos 10.111 dígitos validada.")
    
    # 5. Teste Determinístico de Proth
    # 3^((P-1)/2) = P - 1 (mod P)
    exp = (P - 1) // 2
    print(f"[*] Executando Teste de Proth com base a=3...")
    print(f"    Calculando: 3^((P-1)/2) mod P...")
    t1 = time.time()
    res = pow(3, exp, P)
    t_proth = time.time() - t1
    
    print(f"    Tempo de exponenciação modular: {t_proth:.2f} segundos")
    if res == P - 1:
        print("=" * 75)
        print(">>> RESULTADO: PROVA CONCLUÍDA COM SUCESSO! <<<")
        print(">>> P É UM NÚMERO PRIMO DETERMINÍSTICO LEGÍTIMO (10.111 DÍGITOS). <<<")
        print("=" * 75)
    else:
        print(">>> FALHA: O número não é primo. <<<")
        exit(1)

if __name__ == "__main__":
    verify()
