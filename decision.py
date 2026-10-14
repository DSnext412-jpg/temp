attendance=int(input("Enter attendance percentage: ")) 
marks=int(input("Enter marks: ")) 
 
if attendance<75: 
    print("Decision: Short Attendance") 
elif marks>=40: 
    print("Decision: Pass") 
else: 
    print("Decision: Fail")