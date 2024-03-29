#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class Slopes:
  """
  Attributes:
   - timestamp
   - x
   - y
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'timestamp', None, None, ), # 1
    (2, TType.LIST, 'x', (TType.DOUBLE,None), None, ), # 2
    (3, TType.LIST, 'y', (TType.DOUBLE,None), None, ), # 3
  )

  def __init__(self, timestamp=None, x=None, y=None,):
    self.timestamp = timestamp
    self.x = x
    self.y = y

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.timestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.x = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readDouble();
            self.x.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.y = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readDouble();
            self.y.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Slopes')
    if self.timestamp is not None:
      oprot.writeFieldBegin('timestamp', TType.I64, 1)
      oprot.writeI64(self.timestamp)
      oprot.writeFieldEnd()
    if self.x is not None:
      oprot.writeFieldBegin('x', TType.LIST, 2)
      oprot.writeListBegin(TType.DOUBLE, len(self.x))
      for iter12 in self.x:
        oprot.writeDouble(iter12)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.y is not None:
      oprot.writeFieldBegin('y', TType.LIST, 3)
      oprot.writeListBegin(TType.DOUBLE, len(self.y))
      for iter13 in self.y:
        oprot.writeDouble(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.timestamp is None:
      raise TProtocol.TProtocolException(message='Required field timestamp is unset!')
    if self.x is None:
      raise TProtocol.TProtocolException(message='Required field x is unset!')
    if self.y is None:
      raise TProtocol.TProtocolException(message='Required field y is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
