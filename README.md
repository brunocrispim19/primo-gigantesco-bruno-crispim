# Primo Gigantesco de Bruno de Paula Crispim (10.111 Dígitos)

[![Licence: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Prime Type](https://img.shields.io/badge/Prime-Gigantic_Prime_(10%2C111_digits)-blue.svg)](https://t5k.org/glossary/page.php?sort=GiganticPrime)
[![Proof Method](https://img.shields.io/badge/Proof-Proth's_Theorem_(1878)-green.svg)](https://gallica.bnf.fr/ark:/12148/bpt6k3044v/f788.item)
[![Integrity](https://img.shields.io/badge/SHA--256-b076332f...-orange.svg)](primo_bruno_10111_digitos.txt)

Repositório oficial e documentação técnica da descoberta do número primo gigantesco de **10.111 dígitos decimais** (33.588 bits), ancorado deterministicamente na semente de autoria de **Bruno de Paula Crispim**.

---

## 1. Identificação Matemática

* **Autor:** Bruno de Paula Crispim
* **Classificação Formal:** *Gigantic Prime* (segundo a convenção internacional de [The Prime Pages](https://t5k.org/glossary/page.php?sort=GiganticPrime) para números primos com $N \ge 10^9.999$).
* **Forma Algébrica (Número de Proth):**
  $$P = k^* \cdot 2^33334 + 1$$
* **Multiplicador $k^*$ (77 dígitos decimais / 254 bits):**
  `19000041548667697985925397706689617339423511024733994245427679492849705940689`
* **Hexadecimal de $k^*$:**
  `0x2a01a475c1a0032d83686140d70c158bf6a77b47a071998eb9ea82173b0ff6d1`
* **Expoente Binário ($n$):** `33334` (par, garantindo que $2^n \equiv 1 \pmod 3$)
* **Total de Dígitos Decimais:** `10.111`
* **Comprimento Binário:** `33.588 bits`
* **Hash SHA-256 de Integridade:** `b076332f5e4bd7d252bde6b8bed0079c5286628ad96766287ffa2b7c661f5817`

---

## 2. Ancoragem Criptográfica da Semente

O multiplicador $k^*$ foi derivado deterministicamente a partir da semente de texto exata:
* **String de Entrada:** `"bruno de paula crispim"`
* **Hash SHA-256 [(NIST FIPS 180-4)](https://csrc.nist.gov/publications/detail/fips/180-4/final):**
  `2a01a475c1a0032d83686140d70c158bf6a77b47a071998eb9ea82173b0fa061`
* **Ajuste Algébrico:** O valor inicial derivado do hash foi incrementado pelo crivo modular em $\mathbb{F}_p$ até o primeiro valor satisfazendo $k \equiv 1 \pmod 6$ e sobrevivente de todos os primos $p < 20.000$.

---

## 3. Método de Prova e Rigor Científico

A primalidade de $P$ é demonstrada de maneira **100% determinística** através do [Teorema de Proth (1878)](https://gallica.bnf.fr/ark:/12148/bpt6k3044v/f788.item) e dos critérios de [Brillhart, Lehmer e Selfridge (AMS, 1975)](https://www.ams.org/journals/mcom/1975-29-130/S0025-5718-1975-0384673-1/):

1. **Condição Algébrica:** $k = 19000041548667697985925397706689617339423511024733994245427679492849705940689 < 2^{33334}$ e $k$ é ímpar.
2. **Resíduo Quadrático Incondicional:** Como $n$ é par e $k \equiv 1 \pmod 6$, temos $P \equiv 5 \pmod{12}$ (ou $P \equiv 2 \pmod 3$ e $P \equiv 1 \pmod 4$). Pela Lei da Reciprocidade Quadrática de Gauss:
   $$\left(\frac{3}{P}\right) = \left(\frac{P}{3}\right) (-1)^{(P-1)/2 \cdot (3-1)/2} = \left(\frac{2}{3}\right) (-1)^0 = -1$$
3. **Equivalência Estrita:** Pelo Teorema de Proth, se existir base $a$ tal que $a^{(P-1)/2} \equiv -1 \pmod P$, então $P$ é primo. Como $\left(\frac{3}{P}\right) = -1$, a base $a=3$ é garantida a priori.
4. **Verificação Executada:**
   $$3^{(P-1)/2} \equiv P - 1 \pmod P$$
   Confirmado com sucesso via exponenciação modular por quadrados repetidos (tempo de execução: ~67 segundos em CPU padrão x86_64).

---

## 4. Como Executar a Verificação Independente

Clone o repositório e execute o script Python incluso (não requer bibliotecas externas, usa apenas a biblioteca padrão do Python 3):

```bash
python3 verificar_primo_bruno.py
```

Saída esperada:
```text
===========================================================================
VERIFICAÇÃO DETERMINÍSTICA DO PRIMO DE BRUNO DE PAULA CRISPIM
===========================================================================
[*] Semente textual: 'bruno de paula crispim'
[*] Hash SHA-256 da semente: 2a01a475c1a0032d83686140d70c158bf6a77b47a071998eb9ea82173b0fa061
    [OK] Ancoragem criptográfica verificada com sucesso.
[*] Expoente n = 33334 (par, garantindo 2^n = 1 mod 3)
[*] Multiplicador k = 19000041548667697985925397706689617339423511024733994245427679492849705940689 (k = 1 mod 6, k < 2^n)
    [OK] Premissas de Proth e Reciprocidade Quadrática satisfeitas.
[*] Reconstruindo P = k * 2^n + 1...
    [OK] Reconstruído em 0.0012s.
[*] Total de dígitos decimais: 10111
[*] Comprimento binário: 33588 bits
[*] SHA-256 dos 10.111 dígitos: b076332f5e4bd7d252bde6b8bed0079c5286628ad96766287ffa2b7c661f5817
    [OK] Integridade digital dos 10.111 dígitos validada.
[*] Executando Teste de Proth com base a=3...
    Calculando: 3^((P-1)/2) mod P...
    Tempo de exponenciação modular: 67.81 segundos
===========================================================================
>>> RESULTADO: PROVA CONCLUÍDA COM SUCESSO! <<<
>>> P É UM NÚMERO PRIMO DETERMINÍSTICO LEGÍTIMO (10.111 DÍGITOS). <<<
===========================================================================
```

---

## 5. Estrutura dos Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| `relatorio_primo_bruno.pdf` | Certificado formal de descoberta formatado em LaTeX de alta fidelidade |
| `primo_bruno_10111_digitos.txt` | Expansão integral de todos os 10.111 dígitos decimais formatados |
| `verificar_primo_bruno.py` | Script autônomo de verificação determinística e auditoria |
| `zenodo_metadata.json` | Metadados prontos para registro e geração de DOI no [Zenodo](https://zenodo.org/) |

---

## 6. Referências Acadêmicas

1. **PROTH, François.** *Théorèmes sur les nombres premiers.* Comptes rendus hebdomadaires des séances de l'Académie des sciences (Paris), v. 87, p. 664, 1878. Disponível em: [BNF Gallica](https://gallica.bnf.fr/ark:/12148/bpt6k3044v/f788.item).
2. **BRILLHART, John; LEHMER, Derrick H.; SELFRIDGE, John L.** *New primality criteria and factorizations of $2^m \pm 1$.* Mathematics of Computation (American Mathematical Society - AMS), v. 29, n. 130, p. 620-647, 1975. DOI: [10.1090/S0025-5718-1975-0384673-1](https://www.ams.org/journals/mcom/1975-29-130/S0025-5718-1975-0384673-1/).
3. **CALDWELL, Chris K.** *The Largest Known Primes Database and Glossary.* The University of Tennessee at Martin, 2024. Disponível em: [The Prime Pages](https://t5k.org/glossary/page.php?sort=GiganticPrime).
4. **NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY (NIST).** *FIPS PUB 180-4: Secure Hash Standard (SHS).* U.S. Department of Commerce, 2015. DOI: [10.6028/NIST.FIPS.180-4](https://csrc.nist.gov/publications/detail/fips/180-4/final).
