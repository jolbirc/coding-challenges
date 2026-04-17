def positive_sum(arr):
    return sum(num for num in arr if num > 0)


def basic_test_cases():
    test.assert_equals(positive_sum([1,2,3,4,5]),15)
    test.assert_equals(positive_sum([1,-2,3,4,5]),13)
    test.assert_equals(positive_sum([-1,2,3,4,-5]),9)
        
def empty_case():
    test.assert_equals(positive_sum([]),0)      
    

def negative_case():
    test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)

if __name__ == "__main__":
    basic_test_cases()
    empty_case()
    negative_case()
    