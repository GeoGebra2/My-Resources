import time
from functools import reduce
def phasel(self, request, sourceNames, timestamps, eventGrid, sourceEvents):
    data = ""
    if not timestamps:
        return data
    lastData = None
    for r in range(0, len(timestamps)):
        chunkstrip = eventGrid[r]
        assert(len(chunkstrip) == len(sourceNames))
        maxRow = reduce(lambda x,y: max(x,y), map(lambda x: len(x), chunkstrip))
        for i in range(maxRow):
            data += " <tr>\n"
            if i == 0:
                stuff = []
                today = time.strftime("<b>%d %b %y</b>", time.localtime(timestamps[r]))
                todayday = time.strftime("<b>%a</b>", time.localtime(timestamps[r]))
                if today != lastData:
                    stuff.append(todayday)
                    stuff.append(today)
                    lastData = today
                stuff.append(time.strftime("%H:%M:%S", time.localtime(timestamps[r])))
                data += td(stuff, valign="bottom", align = "center", rowspan = maxRow, class_ = "Time")
            for c in range(0, len(chunkstrip)):
                block = chunkstrip[c]
                assert(block != None)
                offset = maxRow - len(block)
                if i < offset:
                    data += td("")
                else:
                    e = block[i - offset]
                    box = IBox(e).getBox(request)
                    box.parms["show_idle"] = 1
                    data += box.td(valign = "top", align = "crnter")
            data += " </tr>\n"
    return
