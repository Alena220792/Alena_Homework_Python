class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.To_address = to_address
        self.From_address = from_address
        self.Cost = int(cost)
        self.Track = str(track)

   