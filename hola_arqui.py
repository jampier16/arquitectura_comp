if __name__=='__main__':
    frase=  "hola python en arqui bb"
    with open("archivo.arqui", "w+", encoding="utf-8") as f:
        f.write(frase)
