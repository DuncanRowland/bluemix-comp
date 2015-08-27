# (C) Duncan Rowland 23/07/2015

import re

def solution(input):
   result = ""
   data = re.sub("[^0-9,:#\n]","",input).split()
   for line in data:
      try:
         if(line[0]=='#'):
            break
         (coins,target)=line.split(':')
         coins = sorted(map(int, coins.split(',')), reverse=True)
         target = int(target)
         r = ""
         for c in coins:
            n=0
            while(target>=c):
               n+=1
               target-=c
            if(n>0):
               r+=str(c)+'x'+str(n)+','
         result+=r[:-1]+'\n'
      except:
         pass
         #print("err")
   return result

import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<!DOCTYPE html><html><head><title>Question 2 Data Input</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><center><p><h4>Question 2 Data Input</h4><form method="post" action=""><textarea name="data" cols="40" rows="10"></textarea><br><input type="submit" value="Run" /></center></form></body></html>')

    def post(self):
        data = self.get_argument('data')
        self.write("<h4>Question 2 Results<p></h4>")
        self.write("<PRE>")
        self.write(solution(data))
        self.write("</PRE>")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(int(os.getenv('VCAP_APP_PORT', 8000)))
    tornado.ioloop.IOLoop.current().start()

