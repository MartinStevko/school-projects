
class Physics:
    
    def __init__(self):
        self.col_enter = {}
        self.col_stay = {}
        self.col_exit = {}

        pass

    def collide_prepare(self):
        # enter -- becomes --> stay
        for element in self.col_enter:
            self.col_stay[element] = self.col_enter[element]        
        self.col_enter.clear()

        # stay --> stay

        # exit --> none
        self.col_exit.clear()
        
    def collide(self, what = [], against = []):
        for w in what:
            for a in against:
                coll = Physics.AABB(w, a)
                if coll[0]:
                    self.col_enter[ (w, a) ] = coll

    def collide_finish(self):
        exit = {}
        for elem in self.col_stay:
            if elem in self.col_enter.keys():
                del self.col_enter[elem]
            else:
                exit[elem] = self.col_stay[elem]
        for elem in exit:
            del self.col_stay[elem]
            self.col_exit[elem] = exit[elem]

        # raise events
        for elem in self.col_enter:
            self._raise_event(elem[0], elem[1], self.col_enter[elem], "on_collision_enter")
        for elem in self.col_stay:
            self._raise_event(elem[0], elem[1], self.col_stay[elem], "on_collision_stay")
        for elem in self.col_exit:
            self._raise_event(elem[0], elem[1], self.col_exit[elem], "on_collision_exit")        
        
    def _raise_event(self, what, against, coll, name = "on_collision_enter"):
        # REFLECTION MAGIC
        # colliding Ball against Wall will raise "on_collision_enter_Wall"
        handler = getattr(what, name + "_" + against.__class__.__name__, None)
        if handler != None:
            handler(against, coll)

    # AXIS-ALIGNED BOUNDING BOX + collision sides
    @staticmethod    
    def AABB(rect1, rect2):
        collision = rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and rect1.y < rect2.y + rect2.height and rect1.y + rect1.height > rect2.y
        if not collision:
            return (False, None, None, None, None)
        
        # compute penetration
        (north, east, south, west) = (0, 0, 0, 0)

        if rect1.y + rect1.height > rect2.y + rect2.height and rect1.y < rect2.y + rect2.height:
            north = rect2.y + rect2.height - rect1.y
        
        if rect1.y + rect1.height > rect2.y and rect1.y < rect2.y:
            south = rect1.y + rect1.height - rect2.y

        if rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x + rect2.width:
            east = rect2.x + rect2.width - rect1.x

        if rect1.x + rect1.width > rect2.x and rect1.x < rect2.x:
            west = rect1.x + rect1.width - rect2.x

        return (True, north, east, south, west)

        