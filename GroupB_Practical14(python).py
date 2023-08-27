'''
Experiment Number 14: Write a python program to store first year percentage of students in an array.
                      Write function for sorting array of floating point numbers in ascending order using:
                      a) Selection Sort
                      b) Bubble Sort and display top five scores
'''

def Selection_Sort(marks):
    for i in range(len(marks)):
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j
        marks[i], marks[min_idx] = marks[min_idx], marks[i]

    print("Marks of students after performing Selection Sort on the list:")
    for mark in marks:
        print(mark)

def Bubble_Sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Marks of students after performing Bubble Sort on the list:")
    for mark in marks:
        print(mark)

def top_five_marks(marks):
    print("Top", len(marks), "Marks are:")
    print(*marks[::-1], sep="\n")

def main():
    marks = []
    n = int(input("Enter the number of students whose marks are to be displayed: "))
    print("Enter marks for", n, "students (Press ENTER after every student's marks): ")
    for _ in range(n):
        ele = int(input())
        marks.append(ele)

    print("The marks of", n, "students are:")
    print(marks)

    flag = True
    while flag:
        print("\n---------------MENU---------------")
        print("1. Selection Sort of the marks")
        print("2. Bubble Sort of the marks")
        print("3. Exit")
        ch = int(input("\n\nEnter your choice (from 1 to 3): "))

        if ch == 1:
            Selection_Sort(marks)
            a = input("\nDo you want to display top marks from the list (yes/no): ")
            if a == 'yes':
                top_five_marks(marks)
            else:
                print("\nThanks for using this program!")
                flag = False

        elif ch == 2:
            Bubble_Sort(marks)
            a = input("\nDo you want to display top five marks from the list (yes/no): ")
            if a == 'yes':
                top_five_marks(marks)
            else:
                print("\nThanks for using this program!")
                flag = False

        elif ch == 3:
            print("\nThanks for using this program!!")
            flag = False

        else:
            print("\nEnter a valid choice!!")
            print("\nThanks for using this program!!")
            flag = False

if __name__ == "__main__":
    main()
