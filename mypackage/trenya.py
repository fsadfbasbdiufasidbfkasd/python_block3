def make_filter(threshold):
    
    def num_filter(*nums):
        list_num = []
        for num in nums:
            if num >= threshold:
                 list_num.append(num)
            
            
        return list_num
    return num_filter

filter_10 = make_filter(10)

print(filter_10(5, 12, 8, 15, 10))  # [12, 15, 10]
print(filter_10(1, 2, 3))           # []



