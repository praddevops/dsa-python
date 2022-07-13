


class PracticeProblems(): 
      
      def rotated_sorted_list(self, sequence):
          lo, hi = 0, len(sequence)-1
          while lo <= hi:
             mid_position = (lo + hi)//2
             mid_num = sequence[mid_position]
             if lo == hi:
                return mid_poistion
             elif sequence[mid_position-1] > mid_num and mid_num < sequence[mid_position+1]:
                return mid_position
             elif mid_num < sequence[hi]:
                hi = mid_position - 1
             elif mid_num > sequence[hi]:
                lo = mid_position + 1
          return -1