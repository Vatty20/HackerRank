if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    new_list = set(arr)
    new_list.remove(max(new_list)) #removes the max score from list
    
    print(max(new_list))