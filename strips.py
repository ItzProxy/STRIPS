class GroundedCondition:
    def __init__(self, predicate, literals, truth = True):
        self.predicate = predicate
        self.literals = literals
        self.truth = truth

    def reached(self, world):
        return world.is_true(self.predicate, self.literals) == self.truth

    def __str__(self):
        name = self.predicate
        if(not self.truth):
            name = "!" + name
        return "{0}({1})".format(name, join_list(self.literals))

class Actions:
    def __init__(self, name, params, preconditions, postconditions):
        self.name = name
        self.params = params
        self.preconditions = preconditions
        self.postconditions = postconditions
    
    def generate_groundings(self, world):
        self.grounds = []
        current_literals = []
        self.groundings_helper(world.known_literals, current_literals, self.grounds)

    def groundings_helper(self, all_literals, current_literals, grounds):
        if(len(current_literals) == len(self.params)):
            arg_map = dict(zip(self.params, current_literals))
            grounded_precond = [p.ground(arg_map) for p in self.preconditions]
            grounded_postcond = [p.ground(arg_map) for p in self.postconditions]
            grounds.append(GroundedAction(self,current_literals, grounded_precond, grounded_postcond))
            return
        for(literal in all_literals):
            if(literal not in current_literals):
                self.groundings_helper(all_literals, current_literals + [literal], grounds)
        
        def print_grounds(self):
            i = 0
            for(g in self.grounds):
                print("Grounding " + str(i))
                print(grounds)
                i+=1

        def __str__(self):
            return "{0}({1})\nPre: {2}\nPost: {3}".format(self.name, join_list(self.params), join_list(self.preconditions), join_list(self.postconditions))

class GroundedAction:
    def __init__(self, action, literals, preconditions, postconditions):
        self.action = action
        self.literals = literals
        self.preconditions = preconditions
        self.postconditions = postconditions
        self.complete_post_condition = list(postconditions)
        for(p in pre):
            if(not weak_contains(self.complete_post_condition, p)):
                self.complete_post_condition.append(p)
        
    def __str__(self):
        return "{0}({1})\nPre: {2}\nPost: {3}".format(self.action.name, join_list(self.literals), join_list(self.preconditions), join_list(self.postconditions))

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

    def set_true(self, predicate, literals):
        if(predicate not in self.state):
            self.state[predicate] = set()
        self.state[predicate].add(literals)
    
    def set_false(self, predicate, literals):
        if(predicate in self.state):
            self.state[predicate].remove(literals)

    def add_goal(self, predicate, literals, truth=True):
        g = 

    def print(self):
        print("Hello there")

def main():
    w = create_start(None)
    w.print()

if __name__ == "__main__":
    main()