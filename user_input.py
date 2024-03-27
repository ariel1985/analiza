# To get data from user use input() function

print("Something before input function")

input("Text to show before user enters it's data:")

print("Something after the input function")


user_input = input("data to save")
print("User input is: ", user_input)

# בקשו מהמשתמש את השם וקלטו אותו לתוך משתנה 
user_data = input("Enter your name please: ")
print(user_data)
# אם הערך שהמשתמש הקיש הוא אדמין הדפיסו ברוך הבא
if user_data == 'admin':
    print("Welcome!")
# אחרת יש להדפיס ביי ביי
else:
    print('Bye bye..')