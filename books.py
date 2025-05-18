from pymongo import MongoClient
import random

client = MongoClient("mongodb+srv://rajufreelancer789:Raju789@library.lxluagl.mongodb.net/?retryWrites=true&w=majority&appName=Library")

db = client["library"]

collection = db["books"]

collection.delete_many({})

titles = [
    "Mastering MongoDB", "Python Crash Course", "Let Us C", "Operating System Concepts",
    "Introduction to FLAT", "Database Management Systems", "Artificial Intelligence Basics",
    "Machine Learning for Beginners", "Cloud Computing Essentials", "Computer Networks",
    "Advanced Python Programming", "Data Structures in C", "System Design Basics", 
    "Modern Operating Systems", "SQL for Data Analysis", "Networking Fundamentals",
    "Cloud Native Applications", "AI in Practice", "Compiler Design", "Java for Developers",
    "Linux Command Line Basics", "Cyber Security Essentials", "Deep Learning with Python",
    "NoSQL Databases Explained", "Algorithms Unlocked", "Discrete Mathematics", "Blockchain Technology",
    "Android App Development", "Web Development using Flask", "Data Science Handbook",
    "Quantum Computing Basics", "Edge Computing", "Parallel Processing", "IOT Solutions",
    "Information Retrieval Systems", "Agile Software Development", "Software Testing",
    "C++ Primer", "Data Visualization with Python", "Open Source Tools", "AI Ethics",
    "Bioinformatics Computing", "Big Data Analytics", "Python for Data Science", 
    "Digital Image Processing", "Embedded Systems", "Natural Language Processing", 
    "Cloud Security Fundamentals", "Computer Graphics", "Virtual Reality Concepts", "Cryptography Essentials"
]


authors = ["James Clear", "David Beazley", "Yashavant Kanetkar", "Abraham Silberschatz", "Peter Norvig",
           "Andrew Ng", "Evi Nemeth", "Mark Lutz", "Tom White", "Brian Kernighan"]

genres = ["Computer Science", "Programming", "Data Science", "Artificial Intelligence", "Networking"]

books_data = []
for i in range(50):
    book = {
        "title": titles[i],
        "author": random.choice(authors),
        "genre": random.choice(genres),
        "year": random.randint(1995, 2024),
        "isbn": f"978-0-123456-{i+1:02d}"
    }
    books_data.append(book)

collection.insert_many(books_data)

print("✅ 50 CS book documents inserted successfully into 'library.books' collection!")
