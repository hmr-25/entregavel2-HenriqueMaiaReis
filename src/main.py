import cv2
from pathlib import Path
from arquivos import ler_anotacoes

def main():
    pasta_dados = Path("dados")
    pasta_imagens = Path("imagens")
    pasta_resultados = Path("resultados")

   
    pasta_resultados.mkdir(exist_ok=True)

    caminho_csv = pasta_dados / "anotacoes.csv"

    
    imagens_anotadas = ler_anotacoes(caminho_csv, pasta_imagens)

   
    nomes_imagens = sorted(imagens_anotadas.keys())

    for nome_img in nomes_imagens:
        print(f"\nProcessando: {nome_img}")

        caminho_img = pasta_imagens / nome_img
        img = cv2.imread(str(caminho_img))

        if img is None:
            print(f"Erro ao abrir {nome_img}")
            continue

        
        anotada = imagens_anotadas[nome_img].gerar_imagem_anotada(img)

      
        cv2.imshow("Visualizador", anotada)

        print(f"Caixas desenhadas: {len(imagens_anotadas[nome_img].deteccoes)}")

        tecla = cv2.waitKey(0)

        if tecla == ord('q'):
            print("Encerrando execução...")
            break

       
        caminho_saida = pasta_resultados / nome_img
        cv2.imwrite(str(caminho_saida), anotada)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
