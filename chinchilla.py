class Chinchilla:
    def get_chinchillas():
        urls = open("urls.txt", "r")
        clist = []
        for i in urls:
            clist.append(i.replace("\n", ""))
        return clist
