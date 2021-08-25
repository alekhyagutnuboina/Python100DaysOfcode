
steps= int(input('Enter number of steps: '))

steps_list=(input().split()[:steps])

path="".join(steps_list)
print(path)

valleys=0

def countingValleys(steps,path):
    current_level = 0
    valleys = 0
    for i in path:
         if i == 'D':
          current_level=current_level+1
         elif(i=='U'):
           valleys=valleys+1
    return valleys


print("The number of valleys are : " , countingValleys(steps,path))





