import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        


        freq_table = {}
        for num in nums:
            if num in freq_table:
                freq_table[num] += 1
            else:
                freq_table[num] = 1

        # Step 2: Use a min-heap to keep top k frequent elements
        min_heap = []

        for num in freq_table:
            freq = freq_table[num]
            # Push (frequency, number) into heap
            heapq.heappush(min_heap, (freq, num))

            # If heap size > k, remove the smallest frequency item
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: Extract only the numbers from the heap
        result = []
        while min_heap:
            pair = heapq.heappop(min_heap)  # pair = (freq, num)
            result.append(pair[1])          # append just the number

        return result
