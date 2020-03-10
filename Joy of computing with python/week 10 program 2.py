#One day Ajit got a strange feeling of jumping from one point to another. The jumping will be done in one Â­dimension only.
#He will start from a point 0 and from there he will perform a lot of jumps. He can only jump in a specific sequence:
#1Â­jump, 2Â­jump, 3Â­jump, 1Â­jump, 2Â­jump, 3Â­jump, 1Â­jump, and so on. (1Â­>2Â­>3Â­>1Â­>2Â­>3Â­>1.....)

#1-Â­jump means that if Ajit is at the point x, he will jump to the point x+1.
#2Â­-jumps mean that if Ajit is at the point x, he will jump to the point x+2.
#3Â­-jumps mean that if Ajit is at the point x, he will jump to the point x+3.

#get_ipython().set_next_input('Before the start Ajit asks you: will he arrive at the point a after some number of jumps');get_ipython().run_line_magic('pinfo', 'jumps')

#Input Format:
#The first line contains a single number a denoting the point Ajit asks about.

#Output Format:
#Output "YES" without a quotes if Ajit can arrive at point a or "NO" without quotes otherwise.

#Example-1:

#Input:
#0

#Output:
#YES


ip = int(input())
x = ip % 6
if x == 0 or x == 1 or x == 3:
  print("YES", end="")
else:
  print("NO", end="")


x = int(input())

if((x % 6 == 0) or (x % 6 == 1) or (x % 6 == 3)):
    print("YES")
else:
    print("NO")
