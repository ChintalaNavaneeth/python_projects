import lizard
i = lizard.analyze_file("C:/Users/navan/eclipse-workspace/junittests/src/pathtesting/matrtixmultiplication.java")
print(i.__dict__)
print (i.function_list[0].__dict__)
print (i.function_list[1].__dict__)
