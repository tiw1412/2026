
def q_sort(array):
    if len(array) < 2:
        return array

    param = array[0]
    left_array = []
    right_array = []
    middle_array = []

    for i in array:
        if i < param:
            left_array.append(i)
        elif i > param:
            right_array.append(i)
        else:
            middle_array.append(i)
    return q_sort(left_array) + \
           middle_array + \
           q_sort(right_array)

array = [34, 562, 5, 0, 13]
print(q_sort(array))
#config = {
#     'name' : '@citiebotenbotenbot',
#     'token': '8683424936:AAHeg4EQ8hqHxMPqVvi8J0D3QRGuDnU64yM'
# }