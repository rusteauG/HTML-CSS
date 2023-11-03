text = """
What is a database.

A database is a collection of information said and organized so it can be easily accessed, updated, and managed. A relational database or a tabular database is a set of data organized into tables.

You can think of tables as spreadsheets, but it's far more complex in design and can hold millions of rows in order to access the data in relational databases.

We use a language called SQL or structured query language, which we will learn in this course.

Using SQL, a language, we can access our data, update it, run various queries, and get all the data that we need from the database. Databases can be used for various purposes such as sales inventories, employee profiles, student grades, and much more.

Any data that you can store structurally you can use databases. Relational databases are usually managed by a management system or an engine, which controls database users' access and what can and cannot be accessed by those users and groups, as well as managing data reads and writes.

Hence the term Relational Database Management System or RDBMS.
"""

# Replace consecutive newlines with a single newline
text = re.sub(r'\n\n', '\n', text)

print(text)
