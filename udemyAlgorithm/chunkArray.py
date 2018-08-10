def chunkArray(array,sizeofArray):
    result = []
    i = 0
    while(i < len(array)):
        result.append(array[i:i+sizeofArray])
        i = i + sizeofArray

    return result

print(chunkArray([1,2,3,4,5,6,7],7))

#     result =[]
#     chunked = []
#     for i in array:
#         if len(chunked) == sizeofArray:
#             result.append(chunked)
#             chunked = []
#             chunked.append(i)
#         else:
#             chunked.append(i)

#     if chunked:
#         result.append(chunked)

#     return result

# print(chunkArray([1,2,3,4,6,7,12],3))




    # newSizeOfArray = len(array) // sizeofArray
    # newSizeOfArray = newSizeOfArray if len(array)%sizeofArray is 0 else newSizeOfArray+1

#     returnArray = []
#     x = 0

#     for i in range(0, newSizeOfArray):
#         newArray = []
#         for j in range(sizeofArray):
#             if x < len(array):
#                 newArray.append(array[x])
#                 x += 1
#         returnArray.append(newArray)   

#     return returnArray

# print(chunkArray([1,2,3,4,5,6,7],10))

