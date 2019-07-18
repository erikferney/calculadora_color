def crear_log(fn):
    def envoltura(self, txt):
        fn(self, txt)
        print ("Write {}".format(txt))

    return envoltura
