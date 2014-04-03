import pika
import logging
import threading

logging.basicConfig()


class AMQPListener(threading.Thread):
  data_decoder = None
  addr = None
  exch = None
  exch_type = None
  top_key = None
  name = None
  #amqp conn variables
  connection = None
  channel = None
  result = None
  queue_name = None
  count=0
  max_msgs=15
  #threadID = None

  def __init__(self,addr,exch,exch_type,top_key,name,data_decoder):
    print 'Create AMQP Listener ',addr,exch,exch_type,top_key,name
    threading.Thread.__init__(self)
    #self.threadID=threadID
    self.data_decoder = data_decoder
    self.addr=addr
    self.exch=exch
    self.exch_type=exch_type
    self.top_key=top_key
    self.name=name
    self.connection=pika.BlockingConnection( pika.ConnectionParameters(host=addr) )
    #self.connection=pika.SelectConnection (pika.URLParameters(addr), 
    print 'AMQP Connection Created'
    self.channel=self.connection.channel()
    print 'AMQP Channel Created'
    self.channel.exchange_declare( exchange=exch, exchange_type=exch_type )
    print 'Exchanged Declared'
    self.result=self.channel.queue_declare( exclusive=True )
    self.queue_name = self.result.method.queue
    print 'AMQP Prep for Binding to Queue'
    self.channel.queue_bind( exchange=exch,queue=self.queue_name,routing_key=top_key )
    self.channel.basic_consume(self.data_in,queue=self.queue_name,no_ack=True)
    print 'AMQP Listener Constructed'  
  
  def data_in(self,ch,method,properties,body):
    if self.count == self.max_msgs:
       self.stop()
    else:
       self.data_decoder.decode_data( body , properties )
       self.count=self.count+1

  def run(self):
    #print 'Start AMQP Listener ',self.max_msgs
    #self.channel.basic_consume(self.data_in,queue=self.queue_name,no_ack=True)
    print 'Now start consuming'
    self.channel.start_consuming()
    print 'done starting ampq'

  def stop(self):
    print 'Stop AMQP Listener'
    self.channel.stop_consuming()

  def test(self,data):
    print 'AMQP Listener - test with data'
    self.data_decoder.decode_data(data)

