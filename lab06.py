import os
import time

def ler_pla(nome_arquivo):

    num_variaveis = 0
    mintermos = []
    dont_cares = []

    with open(nome_arquivo, "r") as arq:

        for linha in arq:

            linha = linha.split("#")[0].strip()

            if not linha:
                continue

            if linha.startswith(".i"):
                num_variaveis = int(linha.split()[1])

            elif linha.startswith("."):
                continue

            else:

                partes = linha.split()

                if len(partes) < 2:
                    continue

                entrada = partes[0]
                saida = partes[1]

                termos = expandir_entrada(entrada)

                if saida == "1":
                    mintermos.extend(termos)

                elif saida == "-":
                    dont_cares.extend(termos)

    return num_variaveis, sorted(set(mintermos)), sorted(set(dont_cares))


def expandir_entrada(entrada):

    if "-" not in entrada:
        return [int(entrada, 2)]

    pos = entrada.index("-")

    resultado = []

    for bit in ["0", "1"]:

        nova = entrada[:pos] + bit + entrada[pos + 1:]

        resultado.extend(expandir_entrada(nova))

    return resultado


def combinar(a, b):

    diferencas = 0
    resultado = ""

    for x, y in zip(a, b):

        if x == y:
            resultado += x

        else:

            diferencas += 1
            resultado += "-"

            if diferencas > 1:
                return None

    if diferencas == 1:
        return resultado

    return None


def cobre(implicante, mintermo):

    for a, b in zip(implicante, mintermo):

        if a != "-" and a != b:
            return False

    return True


def quine_mccluskey(mintermos, dont_cares, n):

    todos = sorted(set(mintermos) | set(dont_cares))

    termos = [format(m, f"0{n}b") for m in todos]

    primos = []

    while True:

        usados = set()
        novos = []

        for i in range(len(termos)):

            for j in range(i + 1, len(termos)):

                combinado = combinar(termos[i], termos[j])

                if combinado:

                    usados.add(termos[i])
                    usados.add(termos[j])

                    if combinado not in novos:
                        novos.append(combinado)

        for termo in termos:

            if termo not in usados and termo not in primos:
                primos.append(termo)

        if not novos:
            break

        termos = novos

    return primos


def bits_para_expressao(bits):

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resultado = ""

    for i, bit in enumerate(bits):

        if bit == "1":
            resultado += letras[i]

        elif bit == "0":
            resultado += letras[i] + "'"

    return resultado


def expressao_sop(primos):

    return " + ".join(bits_para_expressao(p) for p in primos)


# Atividade 02 - Letra B
def atividade_b(pasta_tests):

    print("\nATIVIDADE 02 - LETRA B")
    print("-" * 50)

    arquivo = os.path.join(
        pasta_tests,
        "ex01_funcao3var.pla"
    )

    n, mintermos, dont_cares = ler_pla(arquivo)

    primos = quine_mccluskey(
        mintermos,
        dont_cares,
        n
    )

    print("Arquivo:", os.path.basename(arquivo))
    print("Mintermos:", mintermos)

    print("Expressao minimizada:")
    print(expressao_sop(primos))


# Atividade 02 - Letra C
def atividade_c(pasta_tests):

    print("\nATIVIDADE 02 - LETRA C")
    print("-" * 50)

    exemplos = [
        ("ex_and.pla", "AB"),
        ("ex01_funcao3var.pla", "A'C' + A'B + BC"),
        ("ex02_funcao4var.pla", "A + B")
    ]

    for arquivo, kmap in exemplos:

        caminho = os.path.join(
            pasta_tests,
            arquivo
        )

        n, mintermos, dont_cares = ler_pla(caminho)

        primos = quine_mccluskey(
            mintermos,
            dont_cares,
            n
        )

        print("\nArquivo:", arquivo)
        print("Karnaugh :", kmap)
        print("QM       :", expressao_sop(primos))


def benchmark(pasta_benchmark):

    print("\nBENCHMARK")
    print("-" * 50)

    for arquivo in sorted(os.listdir(pasta_benchmark)):

        if arquivo.endswith(".pla"):

            caminho = os.path.join(
                pasta_benchmark,
                arquivo
            )

            n, mintermos, dont_cares = ler_pla(caminho)

            inicio = time.time()

            quine_mccluskey(
                mintermos,
                dont_cares,
                n
            )

            fim = time.time()

            tempo = (fim - inicio) * 1000

            print(
                arquivo,
                "-",
                round(tempo, 2),
                "ms"
            )


if __name__ == "__main__":

    BASE = r"C:\Users\Spark\Downloads\lab06\benchmark"

    TESTS = os.path.join(BASE, "tests")
    BENCHMARK = os.path.join(BASE, "benchmark")

    atividade_b(TESTS)
    atividade_c(TESTS)
    benchmark(BENCHMARK)
