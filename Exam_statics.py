def main():
    grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]  # all grades


    def print_grades(grades):                                           #Print all the grades one by one
        for grade in grades:
            print grade



    def grades_sum(grades):                                             #Summing all the grades
        total = 0
        for grade in grades:
            total += grade
        return total


    def grades_average(grades):                                          #Compute average of grades
        sum_of_grades = grades_sum(grades)
        average_of_grades = sum_of_grades / float(len(grades))
        return average_of_grades


    def grades_variance(scores):                                          #Calculte variance
        average = grades_average(scores)
        variance = 0
        for each_score in scores:
            difference = (average - each_score) ** 2
            variance += difference
            result = variance / len(scores)
        return result


    def grades_std_deviation(variance):                                  #Calculate satandard deviation
        return variance ** 0.5


    variance = grades_variance(grades)

    print_grades(grades)                                                 #Print all the functions
    print grades_sum(grades)
    print grades_average(grades)
    print grades_variance(grades)
    print grades_std_deviation(variance)
