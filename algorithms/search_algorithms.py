
class AlgorithmImplementation:

    def linear_search(self, **input):
        # sequence order (ascending or descending does not matter). if multiple occurences of query are found, returns first occurence in the sequence list
        position = 0
        while position < len(input['sequence']):
            if input['sequence'][position] == input['query']:
                return position
            position+=1

        if  position == len(input['sequence']):
            position = -1
        return position


    def test_location(self, sequence, query, middle_position):
        # helper function for binary_search method to help identify multiple occurences of query and help find the first occurence
        mid_number = sequence[middle_position]
        if query == mid_number:
            if middle_position >= 1 and sequence[middle_position - 1] == query:
                return 'left'
            else:
                return 'found'
        elif mid_number > query:
            return 'left'
        elif mid_number < query:
            return 'right' 

    def binary_search(self, **input, condition=self.test_location):
        # sequence is in ascending order
        start_position, end_position = 0, len(input['sequence']) - 1
        query = input['query']
        while start_position <= end_position:
            middle_position = (start_position + end_position)//2
            result = condition(input['sequence'],query,middle_position)
            if result == 'found':
                return middle_position
            elif result == 'left':
                end_position = middle_position - 1
            elif result == 'right': 
                start_position = middle_position + 1
        
        return -1