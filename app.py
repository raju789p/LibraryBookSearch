import streamlit as st
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("Your MongoDB server link/")
db = client["library"]
collection = db["books"]

st.title("📚 Library Book Search (CS Edition)")

search_option = st.selectbox("Search by", ["Title", "Author"])
keyword = st.text_input(f"Enter {search_option}")

if st.button("Search"):
    if search_option == "Title":
        query = {"title": {"$regex": keyword, "$options": "i"}}
    else:
        query = {"author": {"$regex": keyword, "$options": "i"}}

    results = list(collection.find(query))

    if results:
        st.success(f"Found {len(results)} book(s)")
        for book in results:
            st.subheader(book['title'])
            st.write(f"**Author:** {book['author']}")
            st.write(f"**Genre:** {book['genre']}")
            st.write(f"**Year:** {book['year']}")
            st.write(f"**ISBN:** {book['isbn']}")
            st.markdown("---")
    else:
        st.warning("No matching books found.")
