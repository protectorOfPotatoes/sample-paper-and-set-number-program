import pyautogui as pg
import time
subject = input("write the subject for the required sample paper \n")
setNumber = input("write sample paper set number \n")
pg.press('win')
time.sleep(1)
pg.typewrite('chrome')
pg.press('enter')
time.sleep(1)


def subSearch(x, y):
    pg.typewrite(f"https://meritbatch.com/cbse-sample-papers-for-class-10-{x}-set-{y}/")
    pg.press('enter')


if subject != 'hindi' and subject != 'maths' and subject != 'sst':
    subSearch(subject, setNumber)
elif subject == 'maths':
    subSearch('maths-standard', setNumber)
elif subject == 'sst':
    subSearch('social-science', setNumber)
else:
    subSearch('hindi-b', setNumber)
