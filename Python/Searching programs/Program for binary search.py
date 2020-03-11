def binary_search(l, num_find):
    '''
    This function is used to search any number.
    Whether the given number is present in the
    list or not. If the number is present in list
    the list it will return TRUE and FALSE otherwise.
    '''
    start = 0
    end = len(l) - 1
    mid = (start + end) // 2

    # We took found as False that is, initially
    # we are considering that the given number
    # is not present in the list unless proven
    found = False
    position = -1

    while start <= end:
        if l[mid] == num_find:
            found = True
            position = mid
            break

        if num_find > l[mid]:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2

    return (found, position)

    # Time Complexity : O(logn)


# main code
if __name__ == '__main__':

    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 6
    found = binary_search(l, num)
    if found[0]:
        print('Number %d found at position %d' % (num, found[1]+1))
    else:
        print('Number %d not found' % num)
