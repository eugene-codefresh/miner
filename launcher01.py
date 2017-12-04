import os
import datetime
comment = str(datetime.datetime.now())
print('COMMENT: {comment}'.format(comment=comment))
with open('main.py', 'a') as f:
    f.write('\n#'+comment)
os.system('git add -A')
os.system('git commit -a -m "{comment}"'.format(comment=comment))
os.system('git push')