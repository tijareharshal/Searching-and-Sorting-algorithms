import random

class BinarySearch:
    def __init__(self, arr, num):
        self.arr = arr
        self.num = num
        self.l_bound = 0
        self.u_bound = len(self.arr)-1
        print('Original array: ', self.arr)
        print('Element to find: ', self.num)

    def find_element(self):
        while self.l_bound <= self.u_bound:
            mid = (self.l_bound + self.u_bound)//2

            if self.arr[mid] == self.num:
                print(f"Element {self.num} found at index {mid}.")
                break

            else:
                if self.arr[mid] > self.num:
                    self.u_bound = mid - 1
                else:
                    self.l_bound = mid + 1

if __name__ == '__main__':

    sorted_arr = sorted(random.sample(range(0,100),10))
    to_find = random.choice(sorted_arr)

    b1 = BinarySearch(sorted_arr, to_find)
    b1.find_element()
