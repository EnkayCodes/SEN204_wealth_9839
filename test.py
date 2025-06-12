def calculate_cgpa():
    print("CGPA Calculator")
    n = int(input("Enter number of subjects: "))
    
    total_points = 0
    for i in range(1, n+1):
        grade_point = float(input(f"Enter grade point for subject {i} (e.g., 3.5): "))
        total_points += grade_point

    cgpa = total_points / n if n > 0 else 0
    print(f"Your CGPA is: {cgpa:.2f}")

if __name__ == "__main__":
    calculate_cgpa()
