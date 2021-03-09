import easygui
import time 


def getResume():
    print("\nSelect your resume in the pop-up dialog-box (may be hiding behind other open programs)")
    time.sleep(1)
    resume = str('')
    try:
        resume = easygui.fileopenbox()
        print(resume)
        if resume == None:
            print('\nError occured selecting your resume')
            resume = str(input('Please enter the absoulte pathname of your resume including the filename: '))
        resume = str(resume)
    except:
        print('\n Error occured selecting your resume')
        resume = str(input('Please enter the absoulte pathname of your resume including the filename: '))
    return resume
