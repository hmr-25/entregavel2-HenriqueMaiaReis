import cv2

class Deteccao:
    def __init__(self, classe_id, x_min, y_min, x_max, y_max):
        self.classe_id = classe_id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def desenhar(self, imagem):
       
        cor = (0, 255, 0) if self.classe_id == 0 else (255, 0, 0)

        cv2.rectangle(
            imagem,
            (self.x_min, self.y_min),
            (self.x_max, self.y_max),
            cor,
            2
        )


class ImagemAnotada:
    def __init__(self, nome_imagem):
        self.nome_imagem = nome_imagem
        self.deteccoes = []

    def adicionar_detecao(self, det):
        self.deteccoes.append(det)

    def gerar_imagem_anotada(self, imagem):

        
        copia = imagem.copy()
        for det in self.deteccoes:
            det.desenhar(copia)
        return copia
