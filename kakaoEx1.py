import re

st=""
def solution(new_id):
    st=new_id.lower();
    st=re.sub('[^a-z0-9\-_.]','',)
 
    return st




def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

print(solution2('ghkstm##d100#@naver.com##123'))




