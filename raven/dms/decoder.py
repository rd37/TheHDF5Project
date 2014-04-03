import array
import raven.commons.slopes_enc.ttypes as slopes
import raven.commons.audio_enc.ttypes as audio
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

class DataDecoder:
  dec_type = None
  file_wrtr = None
  def __init__(self,type,file_wrtr):
    print 'Create DataDecoder of type ',type
    self.file_wrtr=file_wrtr
    if type=="thrift_encoded":
      self.dec_type=ThriftDecoder()
    if type=="audio_encoded":
      self.dec_type=AudioDecoder()
    if type=="no_encoded":
      self.dec_type=NoDecoder()
    if type=="png_encoded":
      self.dec_type=PNGDecoder()

  def decode_data(self,data,properties):
    self.dec_type.decode_data(data,properties,self.file_wrtr)

class PNGDecoder:
  def __init__(self):
    print 'No Decoder'

  def decode_data(self,data,props,wrtr):
    wrtr.write_img(props.headers["timestamp"],data)


class NoDecoder:
  def __init__(self):
    print 'No Decoder'

  def decode_data(self,data,props,wrtr):
    wrtr.write_data(data)

class ThriftDecoder:
  def __init__(self):
    print 'Thrift Decoder'

  def decode_data(self,data,props,wrtr):
    transportIn = TTransport.TMemoryBuffer(data)
    protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)
    print('now deserialize bytes')
    slps = slopes.Slopes()
    slps.read(protocolIn)
    print 'data ',data
    print 'return raw bytes ',slps.timestamp, slps.x
    print 'obj ',slps 
    #return data
    wrtr.write_data(props.headers["timestamp"],slps.x,slps.y)

class AudioDecoder:
  def __init__(self):
    print 'Audio Decoder'

  def decode_data(self,data,props,wrtr):
    #print 'Data Decoder Audio decoding the data'
    transportIn = TTransport.TMemoryBuffer(data)
    #print 'transport created'
    protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)
    #print('now deserialize bytes')
    aud = audio.Audio()
    aud.read(protocolIn)
    
    #print 'props ',props
    #ts = props.headers["pts"]%1000000000
    #tts = str( props.timestamp  ) + str( ts )
    #print 'ts ',ts,props.timestamp,tts

    #print 'props ',props.headers["pts"]
    #print 'obj info ',aud.channels,aud.rate,aud.sample,len(aud.sample)
    x=[]
    y=[]
    for i in range(0,aud.channels):
        if i < aud.channels/2 :
           x.append(aud.sample[i])
        else:
           y.append(aud.sample[i])
    
    #print 'x ',x
    #print 'y ',y
    wrtr.write_data(props.headers["timestamp"],x,y)
