from search_algorithms import AlgorithmImplementation


class PracticeProblems(AlgorithmImplementation): 
      
      def rotated_sorted_list(self, sequence):
          lo, hi = 0, len(sequence)-1
          while lo < hi:
             mid_position = (lo + hi)//2
             mid_num = sequence[mid_position]
             if mid_position > 0 and sequence[mid_position-1] < mid_num < sequence[mid_position+1]:
                return mid_position
             elif mid_num < sequence[hi]:
                hi = mid_position - 1
             elif mid_num > sequence[hi]:
                lo = mid_position + 1
          return -1          
          