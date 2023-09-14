# 2D Graphical System

## Requisitos

-   PyQt5
-   NumPy

## Execução

```bash
python3 main.py
```

## Usando o Sistema

-   Seleção do tipo do objeto com os botões no menu;
-   Criação dos pontos usando o botão esquerdo do mouse; clicar em "Confirm" para registrar o objeto;
-   Para deletar objetos, selecionar o nome na lista e clicar no botão "Delete";
-   Para cancelar objetos sendo criados, usar o botão "Cancel";
-   O botão "Select color" permite trocar a cor do objeto antes ou após sua criação
-   A caixa de texto abaixo da tela desenhável contém mensagens de log quanto ao uso e estado do programa;
-   Navegação com os botões de seta da interface;
-   Zoom In / Zoom Out com os respectivos botões;

## Edição de objetos

-   Duplo clique sobre os objetos na lista para abrir a tela de edição
-   Selecionar as transformações desejadas e os valores para cada uma
-   Ao final, pressionar "Confirm"
-   Caso desejado, o botão "Reset" move o objeto para sua posição original

## Importando arquivos .obj
-   Criar o arquivo .obj (e .mtl, se necessário) no diretório "objects"
-   Na tela principal, com o campo de inserção de nome de objeto vazio, pressionar "Confirm"
-   Duplo clique sobre o nome do respectivo arquivo o carregará e desenhará os objetos na tela
-   Há também possibilidade de redimensionamento da Window, caso especificado com "w" no arquivo .obj
