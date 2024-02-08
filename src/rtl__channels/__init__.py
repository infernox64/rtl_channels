from .channels import Channel
import json,io,os,re
from os import environ
from os import path
from rtlsdr import RtlSdr
channel_list = list()
class CHANNELS:
    pass
envre = re.compile(r"^(\w+)=(.+)")

__all__ = ['CHANNELS', 'Channel','channel_list','here',RtlSdr]
from pathlib import Path
here = Path(os.path.realpath(path.dirname(__file__)))
envfile = path.join(here,".env")
def load_channels(fname="freq.json"):
    json_file = here / fname
    freq_fd = io.open(json_file,'r')
    freqs_obj = json.load(freq_fd)
    freqs = freqs_obj['root']
    for c in freqs:
        channel_list.append(c)
        cname = c['name']
        exec('{k} = Channel(o)'.format(k=cname,o=c))
        exec('CHANNELS.{k} = {k}'.format(k=cname))
        exec('channel_list.append({k})'.format(k=cname))

if "FREQ_FILE" in os.environ:
    load_channels(os.getenv("FREQ_FILE"))
elif path.exists(envfile):
        envlns = io.open(envfile,'r').readlines()
        for l in envlns:
            if match := envre.match(l):
                var,val = match.groups()
                os.environ[var] = val
                if var == "FREQ_FILE":
                    load_channels(val)
else:
    load_channels()


