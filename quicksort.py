def quicksort(input):
    return _quicksort(input, 0, len(input)-1)

def _quicksort(input, start, end):
    if end <= start:
        return

    pivot = start
    left = pivot+1
    right = end

    while left < right:
        while input[left] < input[pivot] and left < end:
            left += 1
        while input[right] > input[pivot]:
            right -= 1

        if left < right and input[left] > input[right]:
            input[left], input[right] = input[right], input[left]

    if input[right] < input[pivot]:
        input[right], input[pivot] = input[pivot], input[right]

    _quicksort(input, start, right-1)
    _quicksort(input, right+1, end)
    return input
