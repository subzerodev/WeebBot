import sys
sys.path.append(".")
from lib import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont
import logging
import math


#get logger 
logger = logging.getLogger('mainlog')

class eink:
    def __init__(self):
        '''
        Init new object with params
        '''
        #setup image and display

        self.epd = epd2in13_V2.EPD()
        self.epd.init(self.epd.FULL_UPDATE)
        self.image = Image.new('1',(self.epd.height,self.epd.width),255)
        self.draw = ImageDraw.Draw(self.image)

        # Define Constants
        self.axisend = 5
        self.axisoffset = 20
        self.yaxisoffset = 25
        self.xend = 300
        self.yend = 300
        self.xzero = self.xend-self.axisoffset
        self.yzero = self.yend-self.yaxisoffset
        self.ymax = self.axisend
        self.xmax = self.axisend
        self.axisthickness = 2
        self.roundToBase = [5,5]
        self.page =0
        self.maxPages = 100

    def display(self):
        #Updates display
        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.display(self.epd.getbuffer(self.image))

    def fontGrab(self,fontSize):
        #returns font obj of the given font size
        return ImageFont.truetype('/home/discordannoucer/WeebBot/lib/ShadowsIntoLight-Regular.ttf',fontSize)

    def roundTo(self,x,base,up=False,down=False):
        #round number to a certain nearest base
        if(up):
            return math.ceil(float(x)/float(base))*base
        elif(down):
            return math.floor(float(x)/float(base))*base
        else:
            return round(float(x)/float(base))*base

    def stringToPages(self,string,fontSize):
        #displays string on screen and wraps if needed
        #grab font
        self.font_tmp = self.fontGrab(fontSize)
        self.stringFontSize = fontSize

        #split string into array of words
        self.splitString = string.split('},{')
        
       #array to hold pagewise data
        self.pageHold =[]
        self.pageBuffer_tmp = []
        self.pageIndex = 0
        self.page = 0
        self.pageHeight = 500
        self.maxLines = self.roundTo(self.pageHeight/(fontSize+2),1,down=True)
        #logger.debug('MaxLines: ' + str(self.maxLines))

        #Array to hold linewise data
        self.hold_tmp =[]
        index = 0
        self.string_tmp= ''

        #Fill the linewise data array
        for word in self.splitString:
            if(self.font_tmp.getsize(self.string_tmp + word + ' ')[0] < 250):
                self.string_tmp = self.string_tmp + word + ' '
            else:
                self.hold_tmp.append(self.string_tmp)
                self.string_tmp = word + ' '
                
        self.hold_tmp.append(self.string_tmp)

        #fill in the pagewise data arrray
        for line in self.hold_tmp:
            if(self.pageIndex < self.maxLines):
                self.pageBuffer_tmp.append(line)
                
            else:
                self.pageHold.append(self.pageBuffer_tmp)
                self.pageBuffer_tmp = []
                self.pageIndex = -1
            self.pageIndex = self.pageIndex + 1
        self.pageHold.append(self.pageBuffer_tmp)

        #save total nim of pages
        self.maxPages = len(self.pageHold)
        #logger.debug('Max pages: ' + str(self.maxPages))

    def pagesToDisplay(self):
        #displays pages on the screen and displays ui at bottom
        epd = epd2in13_V2.EPD()
        #clean canvas
        self.image = Image.new('1', (epd.height, epd.width),255)
        self.draw = ImageDraw.Draw(self.image)

        #GrabFont
        self.font_tmp = self.fontGrab(self.stringFontSize)

        #Print to the display
        i = 0
        for line in self.pageHold[self.page]:
            self.draw.text((0, i*(self.stringFontSize+2)),line,font=self.font_tmp, fill=0)
            i = i+1

        #grab a font

        self.display()


