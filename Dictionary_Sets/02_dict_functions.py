marks ={
    "sam": 100,
    "ram": 200,
    "Rohan": 23
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"sam":40,"shubham":30})
print(marks)
print(marks.get("sam")) #Prints none if not found