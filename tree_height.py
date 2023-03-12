# python3
# TODO: Create heap and heap sort
# try to achieve  O(n) and not O(n2)

def build_heap(data):
    swaps = []
    n = len(data)

def scan(index):
    min_index = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < n and data[left_index] < data[min_index]:
        min_index = left_index
    
    if right_index < n and data[right_index] < data[min_index]:
        min_index = right_index

    if index != min_index:
        swaps.append((index, min_index))

        data[index], data[min_index] = data[min_index]
        scan(min_index)

for index in range(size // 2,-1,-1):
    scan(index)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    
    text = input("Enter 'I' for input or 'F' for file")
    if 'F' in text:
        file_name = input("Enter file name: ")
        if 'a' not in file_name:
            path = './tests/' + file_name
            with open(path, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))

    # input from keyboard    
    if 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n
       
    # calls function to assess the data 
    # and give back all swaps
    swaps = scan(data))

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= n*4
    
    print(len(swaps))
    for i, j in swaps:
            print(i, j)
    # outputs all swaps

if __name__ == "__main__":
    main()
