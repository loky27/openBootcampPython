def contar (desde,hasta,collback):
    def decrementar(n):
        if n == hasta-1:
            return 0
        else:
            collback(n)
            return decrementar(n-1)
    decrementar(desde)

def main ():
    contar(100,1,print)


if __name__=="__main__":
    main()

