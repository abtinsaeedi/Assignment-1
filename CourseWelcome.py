
#take three inputs
subject = input("what subject do you study?")
courseName = input("whats the course name?")
courseSchedule = input("When is your course")

#three different kinds of strings
helloMsg = "Hello %s world" % subject
courseMsg = " {0} with Python".format(courseName)
seeYouMsg = f'See you on {courseSchedule}'

#display output
print(helloMsg)
print(courseMsg)
print(seeYouMsg)