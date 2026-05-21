class Movie:
    total_movies=0
    def __init__(self,name,director):
        if Movie.check(name):

            self.name=name
            self.director=director
            Movie.total_movies+=1
        else:
            print("Invalid")
    @classmethod
    def string(cls,x):
        name,director=x.split("-")
        return cls(name,director)
    @staticmethod
    def check(name):
        return len(name)>=4
e1=Movie("mani","ramya")
e2=Movie("mani1","ramya2")
print({e2.name},{e2.director})
