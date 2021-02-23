


class Aromat:
    def __int__(self, item_aromat):
        self.item_aromat = list(item.aromat)
        def __getattr__(self, i):
            return self.item_aromat[i]


class Diffuser:
     def __init__(self):
      self.work = 0

     def diffuser(self, item_aromat, room):
       for i in room:
         i.take(item_aromat)
         self.work += 1

class Room:
    def __init__(self):
      self.aroma_room=[]

    def take(self, item_aromat):
      self.aroma_room.append(item_aromat)


