if __name__ == '__main__':
    import gevent.monkey
    import time
    import contas
    gevent.monkey.patch_all()
    import verify_deletion
    from random import shuffle

    while True:
        arrobas = contas.pega_contas()
        arrobas.remove("acaciofavacho")
        shuffle(arrobas)
        print("Checando se tweets foram removidos...")
        start_time = time.time()
        verify_deletion.verify(arrobas)
        end_time = time.time()
        print("Terminado em... ")
        print(end_time - start_time)

