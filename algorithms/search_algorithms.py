
class AlgorithmImplementation:

    def linear_search(self, **input):
        position = 0
        while position < len(input['sequence']):
            if input['sequence'][position] == input['query']:
                return position
            position+=1

        if  position == len(input['sequence']):
            position = -1
        return position