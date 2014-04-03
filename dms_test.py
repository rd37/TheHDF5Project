import raven.dms.dms as dmp
import sys

print 'creating dms and setting ampq max mesages ',str(sys.argv[1]),str(sys.argv[2])
dms=dmp.DMS(str(sys.argv[1]))

for amqp_src in dms.amqp_ptr:
  amqp_src.max_msgs= int( sys.argv[2] )
  amqp_src.start()

for t in dms.amqp_ptr:
  t.join()

print 'done see ya ',sys.argv[2]
