fruits = ["apple","banana","cherry","date"]
fruits.append("elderberry")
fruits.remove("banana")
fruits.sort()
#print(fruits)

student = {}
student['name'] = 'John Doe'
student['age'] = 25
student['major'] = 'Computer Science'
student['major'] = 'Electrical Engineering'
student['year'] = 'Senior'
#print(student.keys())

books_ls = []
white_fang = {'title':'White Fang', 'author':'Jack London', 'year':1906}
book_1984 = {'title':'1984', 'author':'George Orwell', 'year':1949}
name_rose = {'title':'The Name of the Rose', 'author':'Umberto Eco','year':1980}
books_ls.append(white_fang)
books_ls.append(book_1984)
books_ls.append(name_rose)
#print(books_ls[1]['title'])
#for i, entry in enumerate(books_ls):
    #print(f"The title is \"{entry['title']}\" and the author is {entry['author']}")

courses = {
    "Math": [],
    "History": [],
    "Chemistry": []
}
courses["Math"].append("John Smith")
courses["Math"].append("Tim Johnson")
courses["Math"].append("Ivan Ivanov")
courses["Math"].append("Vladimir Popov")
courses["Math"].append("Franz Spencer")
courses["History"].append("Franz Joseph")
courses["History"].append("Mark Anthony")
courses["History"].append("Octavian August")
courses["Chemistry"].append("Venkatesh Tungala")
courses["Chemistry"].append("Akanksha Sharma")
del courses["History"][2]
courses["Physics"] = "Veselin Stoyanov"
print(courses['History'])
