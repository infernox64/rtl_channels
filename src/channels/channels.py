from enum import Enum
from rtlsdr import RtlSdr
class Channel(object):
    def __init__(self,conf):
        self._conf = conf
        self.name = conf.get('name')
        self.freq = conf.get("frequency")
        self.bandwidth = conf.get("bandwidth")
        self.bw = self.bandwidth
    def __repr__(self) -> str:
        return str(repr(self._conf))
    def tune(self,rtl: RtlSdr):
        try:
            rtl.set_bandwidth(self.bw)
            rtl.set_center_freq(self.freq)
        except Exception as e:
            raise e



class CHANNELS:
    pass

