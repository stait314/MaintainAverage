
# Two Missing Values
# Finding total value of B (worth 2 values), using set A, to maintain average C

A = (93, 96, 95, 89, 94)                                  # set current scores
C = (95)                                                  # set desired average
B = (C*(len(A) +2)) - (sum(A))          			      # formula for calculating B
print("the total value of B is")                          # sentence 1
print(B)	                                              # print total B value
D = ((B)/2)                                               # 2 singular grades
print("so, you could earn two grades of:")                # sentence 
print(D)                                                  # print value of D (B as 2 grades)