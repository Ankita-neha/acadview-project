print "                  Hey there! Here you can view my python programs"
print "Following are some of my python programs,choose which one you want to run: \n\
1.Student_becomes_the_teacher \n\
2.Battleship \n\
3.Exam_statics \n\ "
selection = raw_input("select the program you want to run:")
if selection == '1':
    import Student_becomes_the_teacher
    Student_becomes_the_teacher.main()
elif selection == '2':
    import Battleship
    Battleship.main()
elif selection == '3':
    import Exam_statics
    Exam_statics.main()
else:
    print "does not exist"


