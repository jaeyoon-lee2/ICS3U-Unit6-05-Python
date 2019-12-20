#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Dec 2019
# This program finds the average of marks


def main():
    # this function uses a list to calculate the average of marks

    marks = []
    each_mark = None
    total = 0

    # input
    print("Please enter your marks at a time. Enter '-1' to end.")

    each_mark = input("Enter a mark: ")
    marks.append(each_mark)
    while each_mark != "-1":
        each_mark = input("Enter a mark: ")
        marks.append(each_mark)

    marks.pop()  # remove the "-1" that was added
    print("")

    for counter in range(0, len(marks)):
        total += int(marks.pop())

    average = total / (counter + 1)
    print("The average of your marks is: {0}".format(average))


if __name__ == "__main__":
    main()
