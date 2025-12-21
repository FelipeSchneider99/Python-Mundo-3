def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(txt.center(tam))
    print('~' * tam)

escreva('Hello, World!')