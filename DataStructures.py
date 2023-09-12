class node:
    def __init__(self,id,label=None,color="#FFB880"):
        self.id=id
        self.label=label
        self.color=color
    def __str__(self):
        result=f'id:{self.id}, label:{self.label}, color:{self.color}'
        return result
class edge:
    def __init__(self,_from,_to,label):
        self._from=_from
        self._to=_to
        self.label=label
