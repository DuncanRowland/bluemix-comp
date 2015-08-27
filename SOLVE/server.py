# (C) Duncan Rowland 23/07/2015

import re

def getTerms(s):
#NxSMy=R
   xP = s.find('x')
   yP = s.find('y')
   eP = s.find('=')
   N=s[0:xP]
   if(N==''):
      N=1
   M=s[xP+1:yP]
   if(M=='+'):
      M=1
   if(M=='-'):
      M=-1
   R=s[eP+1:]
   return [int(N),int(M),int(R)]

def det(D):
   return D[0][0]*D[1][1] - D[0][1]*D[1][0]

def solution(input):
   result = ""
   data=re.sub("[^0-9xy+-=\n]","",input).split()
   for (e1,e2) in zip(data[::2], data[1::2]):
      try:
         t1=getTerms(e1)
         t2=getTerms(e2)
         D  = [[t1[0],t1[1]],[t2[0],t2[1]]]
         Dx = [[t1[2],t1[1]],[t2[2],t2[1]]]
         Dy = [[t1[0],t1[2]],[t2[0],t2[2]]]
         #detD  = float(det(D))
         detD = det(D) #since x and y are integers
         x = det(Dx)/detD
         y = det(Dy)/detD
         result+="x="+str(x)+" y="+str(y)+'\n'
      except:
         pass
         #print("err")
   return result

import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<!DOCTYPE html><html><head><title>Question 3 Data Input</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><center><p><h4>Question 3 Data Input</h4><form method="post" action=""><textarea name="data" cols="40" rows="10"></textarea><br><input type="submit" value="Run" /></center></form></body></html>')

    def post(self):
        data = self.get_argument('data')
        self.write("<h4>Question 3 Results<p></h4>")
        self.write("<PRE>")
        self.write(solution(data))
        self.write("</PRE>")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(int(os.getenv('VCAP_APP_PORT', 8000)))
    tornado.ioloop.IOLoop.current().start()

