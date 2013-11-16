def test():
    import Image
    import ImageDraw
    import ImageFont
    import random
    import md5
    import time,datetime
    dt = datetime.datetime.now()
    im, draw = None, None
    font = ImageFont.truetype('LCALLIG.TTF', 16) 
    
    m_md5 = md5.new()
    m_md5.update( str(dt) )
    rand_str = m_md5.hexdigest()[:4]
    
    im = Image.new('RGB', (60,30), '#000000') 
    draw = ImageDraw.Draw(im) 
    draw.text((10,5), rand_str, font=font) 
    fpath = '%s.jpg' % rand_str
    fp = file(fpath, 'wb')
    im.save(fp,"JPEG")
    fp.close()
if __name__ == '__main__':
    print test()
	
# Traceback (most recent call last):
  # File "Verification_Code.py", line 23, in <modul
    # print test()
  # File "Verification_Code.py", line 7, in test
    # dt = datetime.datetime.now()
# NameError: global name 'datetime' is not defined