# Check whether the keys 'name' and 'grade' exist in the following dictionary:

student = {
    "id": 123,
    "grade": "B",
}
print(student.get("name"))  # None, default return value if doesnt exist
print(student.get("grade"))  # "B"

# OR could use "in"
print("name" in student)  # False
print("grade" in student)  # True
