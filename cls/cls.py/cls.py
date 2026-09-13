# ### 1)

# მოცემულია:

# ```python
# text = "I study Python every day"
# ```

# `replace()` მეთოდის გამოყენებით `"Python"` შეცვალე `"Java"`-თი.

# ---
text = "I study Python every day"
print(text.replace("Python", "Java"))
# ### 2)

# მომხმარებელს შემოატანინე სახელი და გამოიტანე მისი სახელი **დიდი ასოებით**.

# ---
name=input("Enter your name: ")
print(name.upper())
# ### 3)

# მოცემულია:

# ```python
# text = "   Good morning   "
# ```

# `strip()` მეთოდის გამოყენებით მოაშორე ზედმეტი space-ები და დაბეჭდე მიღებული ტექსტი.

# ---
text = "   Good morning   "
print(text.strip())
# ### 4)

# მოცემულია:

# ```python
# text = "my favorite programming language"
# ```

# `title()` მეთოდის გამოყენებით ტექსტი გადაიყვანე შემდეგ ფორმატში:

# ```text
# My Favorite Programming Language
# ```

# ---
text = "my favorite programming language"
print(text.title())
# ### 5)

# მოცემულია:

# ```python
# words = ["Today", "is", "Friday"]
# ```

# `join()` მეთოდის გამოყენებით სიტყვები შეაერთე `" "` გამყოფით.

# ---
words = ["Today", "is", "Friday"]
word=" ".join(words)
print(word)
# ### 6)

# მოცემულია:

# ```python
# numbers = ["5", "10", "15", "20"]
# ```

# `join()` მეთოდის გამოყენებით მიიღე:

# ```text
# 5,10,15,20
# ```

# ---
nums = ["5", "10", "15", "20"]
num=",".join(nums)
print(num)
# ### 7)

# მოცემულია:

# ```python
# text = "Computer Science"
# ```

# slicing-ის გამოყენებით გამოიტანე ტექსტის პირველი **8 სიმბოლო**.
# )
# მოცემულია:
text = "Computer Science"
print(text[:8])
# text = "Development"

# slicing-ის გამოყენებით გამოიტანე ტექსტის ბოლო 5 სიმბოლო.
text = "Development"
print(text[6:])
# ---


# 9)
# მოცემულია:

# words = ["red", "green", "blue"]


# join() მეთოდის გამოყენებით მიიღე:

# red | green | blue


# ---
colour = ["red", "green", "blue"]
coulors=" | ".join(colour)
print(coulors)

# 10)
# მოცემულია:

# text = "PYTHON programming"


# lower() მეთოდის გამოყენებით მთელი ტექსტი გადაიყვანე პატარა ასოებში, შემდეგ slicing-ის 
# გამოყენებით გამოიტანე მხოლოდ პირველი 6 სიმბოლო.

# მოსალოდნელი შედეგი:

# python
text = "PYTHON programming"
print(text.lower())
print(text[:6])