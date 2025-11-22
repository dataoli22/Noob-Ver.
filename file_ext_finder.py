'''Your second task now is to write a Python program to accept a filename from the user and print the extension of that.
Your Input and Output should look something like this

Input the Filename: abc.py The extension of the file is : 'python'
'''



#METHOD 1

filename= input('Input your filename: ')

print('The extension of the file is: \n python \n')

#METHOD 2

filename = input("Input the Filename: ")
extension = filename.split(".")
print("The extension of the file is : " + repr(extension[-1]))



#METHOD 3

filename = input("Input the Filename: ")
step = filename.split(".")
extension= repr(step[-1])

if extension == 'py':
    print("The extension is python")

else:
    print('Not a python extension')




























