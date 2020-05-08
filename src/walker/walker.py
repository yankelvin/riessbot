import random
from .walker_map import map_maze


class Walker:
    def __init__(self):
        self.map_maze = map_maze

    def Generate_Way(self, first_state, objective_state, _type):
        visited = [first_state]
        result = [first_state]
        state_ = first_state
        value_ = 0
        count_cost = 0

        control = {
            state_: {
                'sequence': [first_state],
                'cost': value_
            }
        }

        not_visited = []
        destiny_point = self.map_maze[objective_state]['point']

        while state_ != objective_state:
            not_visited.extend(
                self.__get_adjacent_not_visited(state_, visited))

            if len(not_visited) != 0:
                if _type == 0:
                    selected_state = random.choice(not_visited)
                elif _type == 1:
                    selected_state = self.__uniform_cost(not_visited, control)
                elif _type == 2:
                    selected_state = self.__greedy(
                        not_visited, control, destiny_point)
                elif _type == 3:
                    selected_state = self.__a_star(
                        not_visited, control, destiny_point)

                state_ = selected_state[0]
                value_ = selected_state[1]
                visited.append(state_)
                count_cost += value_
                result.append(state_)

                control[state_] = {
                    'sequence':  control[selected_state[2]]['sequence'][:],
                    'cost': value_ + control[selected_state[2]]['cost']
                }

                control[state_]['sequence'].append(state_)

                not_visited.remove(selected_state)
            else:
                del result[-1]
                state_ = result[-1]
                count_cost -= value_

        return {'sequence': control[objective_state]['sequence'], 'cost': control[objective_state]['cost']}

    def __get_adjacent_not_visited(self, state_, visited):
        states = self.map_maze[state_]
        return_ = []

        for s in states['adjacent']:
            if s[0] not in visited:
                return_.append([s[0], s[1], state_])

        return return_

    def __uniform_cost(self, states, control):
        less_value = float('Inf')
        less_state = states[0]

        if len(states) == 1:
            return states[0]

        for s in states:
            s_cost = control[s[2]]['cost'] + s[1]
            less_cost = control[less_state[2]]['cost'] + less_value
            if s_cost < less_cost:
                less_value = s[1]
                less_state = s

        return less_state

    def __greedy(self, states, control, destiny):
        less_value = float('Inf')
        less_state = states[0]

        if len(states) == 1:
            return states[0]

        for s in states:
            s_point = self.map_maze[s[0]]['point']

            dist = ((destiny[0] - s_point[0])**2 +
                    (destiny[1] - s_point[1])**2)**(0.5)

            if dist < less_value:
                less_value = dist
                less_state = s

        return less_state

    def __a_star(self, states, control, destiny):
        less_value = float('Inf')
        less_state = states[0]

        if len(states) == 1:
            return states[0]

        for s in states:
            s_point = self.map_maze[s[0]]['point']
            less_cost = control[less_state[2]]['cost'] + less_value

            s_cost = control[s[2]]['cost'] + s[1]
            dist = ((destiny[0] - s_point[0])**2 +
                    (destiny[1] - s_point[1])**2)**(0.5)

            if (s_cost + dist) < (less_cost + less_value):
                less_value = dist
                less_state = s

        return less_state


# _type = 0 (Random) | 1 (Uniform Cost) | 2 (Greedy) | 3 (A-Star)
# walker = Walker()
# result = walker.Generate_Way('A', 'Q', _type=1)

# print(f"Caminho resultante: {result['sequence']}")
# print(f"Custo do caminho: {result['cost']}")
