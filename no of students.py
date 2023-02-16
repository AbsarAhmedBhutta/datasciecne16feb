Total_No_Students = input("Enter Total Number of Students:")
Total_No_Biology_Students = input("Enter Total Number of biolgy Students:")
Total_No_Math_Students = input("Enter Total Number of Math Students:")

print(Total_No_Students, "Total_No_Students")
print(Total_No_Biology_Students, "Total_No_Biology_Students")
print(Total_No_Math_Students, "Total_No_Math_Students")

sum_of_bio_and_math_stds = int(Total_No_Math_Students)+int(Total_No_Biology_Students)
Remaining_Stds = int(Total_No_Students)-int(sum_of_bio_and_math_stds)

print(sum_of_bio_and_math_stds, "sum_of_bio_and_math_stds")
print(Remaining_Stds, "Remaining_Stds")

