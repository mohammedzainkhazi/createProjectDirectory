import os
from aicommunication import speak,listen


def createFile(PATH,filename):
	p = os.path.join(PATH,filename)
	try:
		print(f'Creating HTML {filename}\n')
		open(p,'x')
		print(f'Created {filename}\n')
		speak(f'Created {filename}\n')
	except Exception as e:
		print(f'{filename} is Present Already !\n')
		speak(f'{filename} is Present Already !')


def verify():
	pname = listen()
	print(f'{ pname}, is this right Sir?')
	speak(f'{ pname}, is this right Sir?')
	ans = listen()
	if 'no' in ans:
		speak('Please type it Sir\n')
		pname = input()
	else:
		speak(f'{pname} creating')
	return pname

def makeWebsite():
	PATH = 'C:\\Users\\User\\Desktop\\webprojects'
	print('What is the project name Sir?')
	speak('What is the project name Sir')
	pname = verify()
	path = os.path.join(PATH,pname)
	try:
		os.mkdir(path)
	except Exception as e:
		print('Root Directory is already present')
		speak('Root Directory is already present')

	try:
		createFile(path,'index.html')
		createFile(path,'script.js')
		createFile(path,'style.css')
		print("\nCreated All Files !")
		speak("\nCreated All Files !")
	except Exception as e:
	        print(e)



if __name__ == '__main__':
	makeWebsite()        
