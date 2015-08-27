# (C) Duncan Rowland 23/07/2015

factorials = ["1"]
for x in range(1, 16):
   factorials.append(str(int(factorials[x-1])*x))

def solution(input):
   result = ""
   data = input.split()
   for line in data:
      if(line[0]=='#'):
         break
      try:
         result+=factorials[int(line)]+'\n'
      except:
         pass
         #print("err")
   return result

import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<!DOCTYPE html><html><head><title>Question 1 Data Input</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><center><p><h4>Question 1 Data Input</h4><form method="post" action=""><textarea name="data" cols="40" rows="10"></textarea><br><input type="submit" value="Run" /></center></form></body></html>')

    def post(self):
        data = self.get_argument('data')
        self.write("<h4>Question 1 Results<p></h4>")
        self.write("<PRE>")
        self.write(solution(data))
        self.write("</PRE>")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(int(os.getenv('VCAP_APP_PORT', 8000)))
    tornado.ioloop.IOLoop.current().start()

