class ParseState:
    INITIAL=1
    GOAL=2
    ACTION=3
    ACTION_DECLARATION=4
    ACTION_PRE=5
    ACTION_POST=6

def create_start(filename):
    w = World()
    
    return w

class World:

    def __init__(self):
        self.state = dict()
        self.goals = set()
        self.known_literals = set()
        self.actions = dict()

    def is_true(self, predicate, literals):
        if predicate not in self.state:
            return False
        return literals in self.state[predicate]

    def is_false(self, predicate,literals):
        return not self.is_true(predicate,literals)

    def print(self):
        print("Hello there")

def main():
    w = create_start(None)
    w.print()

if __name__ == "__main__":
    main()