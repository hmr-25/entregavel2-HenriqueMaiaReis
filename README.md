# Entregável 2 - Anotação de Imagens com OpenCV

## Descrição

Este projeto realiza a leitura de anotações armazenadas em um arquivo CSV e desenha caixas delimitadoras (bounding boxes) sobre imagens utilizando OpenCV.

As anotações contêm:

- Nome da imagem
- Classe do objeto
- Coordenadas da caixa delimitadora

As imagens anotadas são salvas na pasta `resultados`.

## Como executar

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente

```bash
venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar o projeto

```bash
python src/main.py
```

## Tecnologias utilizadas

- Python
- OpenCV
