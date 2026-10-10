import csv
from pathlib import Path
from modelos import Deteccao, ImagemAnotada
import cv2

def ler_anotacoes(caminho_csv, pasta_imagens):
    """
    Lê o CSV de anotações, valida coordenadas e agrupa Deteccao por imagem.
    Retorna um dicionário: { nome_imagem: ImagemAnotada }
    """

    anotacoes_por_imagem = {}

    caminho_csv = Path(caminho_csv)
    pasta_imagens = Path(pasta_imagens)

    if not caminho_csv.exists():
        raise FileNotFoundError(f"Arquivo CSV não encontrado: {caminho_csv}")

    with caminho_csv.open(newline="", encoding="utf-8") as f:
        leitor = csv.reader(f)
        cabecalho = next(leitor, None)

        if cabecalho is None:
            raise ValueError("CSV vazio ou inválido.")

        for linha in leitor:
            if len(linha) != 6:
                raise ValueError(f"Linha inválida no CSV: {linha}")

            nome_img, classe_id, x_min, y_min, x_max, y_max = linha

            # Conversões
            try:
                classe_id = int(classe_id)
                x_min = int(x_min)
                y_min = int(y_min)
                x_max = int(x_max)
                y_max = int(y_max)
            except ValueError:
                raise ValueError(f"Campos numéricos inválidos na linha: {linha}")

            # Verificar se a imagem existe
            caminho_img = pasta_imagens / nome_img
            if not caminho_img.exists():
                raise FileNotFoundError(f"Imagem não encontrada: {caminho_img}")

            # Carregar imagem para validar coordenadas
            img = cv2.imread(str(caminho_img))
            if img is None:
                raise ValueError(f"Erro ao abrir imagem: {caminho_img}")

            altura, largura = img.shape[:2]

            
            if not (0 <= x_min < x_max < largura):
                raise ValueError(f"Coordenadas X inválidas na linha: {linha}")

            if not (0 <= y_min < y_max < altura):
                raise ValueError(f"Coordenadas Y inválidas na linha: {linha}")

          
            det = Deteccao(classe_id, x_min, y_min, x_max, y_max)

            # Criar ou adicionar ao objeto ImagemAnotada
            if nome_img not in anotacoes_por_imagem:
                anotacoes_por_imagem[nome_img] = ImagemAnotada(nome_img)

            anotacoes_por_imagem[nome_img].adicionar_detecao(det)

    return anotacoes_por_imagem