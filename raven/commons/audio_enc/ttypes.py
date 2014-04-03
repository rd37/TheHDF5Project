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


class Layout:
  INTERLEAVED = 0
  NON_INTERLEAVED = 1

  _VALUES_TO_NAMES = {
    0: "INTERLEAVED",
    1: "NON_INTERLEAVED",
  }

  _NAMES_TO_VALUES = {
    "INTERLEAVED": 0,
    "NON_INTERLEAVED": 1,
  }


class Audio:
  """
  Attributes:
   - timestamp
   - rate
   - channels
   - layout
   - sample
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'timestamp', None, None, ), # 1
    (2, TType.I32, 'rate', None, None, ), # 2
    (3, TType.I32, 'channels', None, None, ), # 3
    (4, TType.I32, 'layout', None,     0, ), # 4
    None, # 5
    (6, TType.LIST, 'sample', (TType.DOUBLE,None), None, ), # 6
  )

  def __init__(self, timestamp=None, rate=None, channels=None, layout=thrift_spec[4][4], sample=None,):
    self.timestamp = timestamp
    self.rate = rate
    self.channels = channels
    self.layout = layout
    self.sample = sample

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
        if ftype == TType.I32:
          self.rate = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.channels = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.layout = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.sample = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readDouble();
            self.sample.append(_elem5)
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
    oprot.writeStructBegin('Audio')
    if self.timestamp is not None:
      oprot.writeFieldBegin('timestamp', TType.I64, 1)
      oprot.writeI64(self.timestamp)
      oprot.writeFieldEnd()
    if self.rate is not None:
      oprot.writeFieldBegin('rate', TType.I32, 2)
      oprot.writeI32(self.rate)
      oprot.writeFieldEnd()
    if self.channels is not None:
      oprot.writeFieldBegin('channels', TType.I32, 3)
      oprot.writeI32(self.channels)
      oprot.writeFieldEnd()
    if self.layout is not None:
      oprot.writeFieldBegin('layout', TType.I32, 4)
      oprot.writeI32(self.layout)
      oprot.writeFieldEnd()
    if self.sample is not None:
      oprot.writeFieldBegin('sample', TType.LIST, 6)
      oprot.writeListBegin(TType.DOUBLE, len(self.sample))
      for iter6 in self.sample:
        oprot.writeDouble(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.timestamp is None:
      raise TProtocol.TProtocolException(message='Required field timestamp is unset!')
    if self.rate is None:
      raise TProtocol.TProtocolException(message='Required field rate is unset!')
    if self.channels is None:
      raise TProtocol.TProtocolException(message='Required field channels is unset!')
    if self.layout is None:
      raise TProtocol.TProtocolException(message='Required field layout is unset!')
    if self.sample is None:
      raise TProtocol.TProtocolException(message='Required field sample is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)