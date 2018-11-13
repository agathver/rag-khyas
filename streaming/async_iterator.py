class AsyncIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.__next = None

        self.__run = False

    def start(self):
        self.__run = True
        
        self.__t = Thread(target=self.update)
        self.__t.daemon = True
        self.__t.start()


    def update(self):
        while self.__run:
            self.__next = next(self.__client)

    def stop(self):
        self.__run = False

    def __iter__(self):
        while self.__run and not self.__next:
            sleep(1)
        
        while True:
            yield self.__next