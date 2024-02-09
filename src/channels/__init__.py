from .channels import Channel
from .freqs import freq_list
import json,io,os,re
from os import environ
from os import path
from rtlsdr import RtlSdr
channel_list = list()
class CHANNELS:
    pass


__all__ = ['CHANNELS', 'Channel','channel_list','here',RtlSdr,'freq_list']
from pathlib import Path
here = Path(os.path.realpath(path.dirname(__file__)))
envfile = path.join(here,".env")
def load_channels(freqs_list):
    
    for c in freqs_list:
        channel_list.append(Channel(c))
        cname = c['name']
        exec('{k} = Channel(o)'.format(k=cname,o=c))
        exec('CHANNELS.{k} = {k}'.format(k=cname))
        exec('channel_list.append({k})'.format(k=cname))



load_channels(freq_list)


