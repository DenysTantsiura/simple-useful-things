#from loguru import logger

#logger.debug("tibasl")

#lll=[ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me' ] ], 'hey.py']
lll=['C:', 'backup.log', 'ideas.txt', ['find.me']]
mmm='find.me'
vma=None
if str(lll).find(mmm)!=-1:
    print(str(lll))
    print(str(lll).find(mmm))
    try:
        vma=lll.index(mmm)
    except:
        vma=0
print(vma)
