print("""Search by:
1. Category
2. System
3. Date
4. Company (?)
      """)

print("Top view a category, please enter its corresponding number")
print("Categorises:")
print("""
1. News
2. Malware
3. Tools
""")

i = input(">>> ")

if i == "2":
    print(""" Show 
1. Windows: 200 hits
2. OSX:     76 hits
3. Linux:   41 hits
4. Other:   80 hits
    """)
