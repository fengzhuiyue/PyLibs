#!/usr/bin/env python
#-*-coding:utf-8-*-
from sgmllib import SGMLParser
import htmlentitydefs

class BaseHTMLProcessor(SGMLParser):
    def reset(self):                       
        # extend (called by SGMLParser.__init__)
        self.pieces = []
        SGMLParser.reset(self)
    
    #是一个开始一个块的 HTML 标记，象 <html>，<head>，<body> 或 <pre> 等，或是一个独一的标记，
    #象 <br> 或 <img> 等。当它找到一个开始标记 tagname，SGMLParser 将查找名为 start_tagname
    #或 do_tagname 的方法。例如，当它找到一个 <pre> 标记，它将查找一个 start_pre 或 do_pre 的方法。
    #如果找到了，SGMLParser 会使用这个标记的属性列表来调用这个方法；否则，它用这个标记的名字和属性
    #列表来调用 unknown_starttag 方法。
    def unknown_starttag(self, tag, attrs):
        # called for each start tag
        # attrs is a list of (attr, value) tuples
        # e.g. for <pre class="screen">, tag="pre", attrs=[("class", "screen")]
        # Ideally we would like to reconstruct original tag and attributes, but
        # we may end up quoting attribute values that weren't quoted in the source
        # document, or we may change the type of quotes around the attribute value
        # (single to double quotes).
        # Note that improperly embedded non-HTML code (like client-side Javascript)
        # may be parsed incorrectly by the ancestor, causing runtime script errors.
        # All non-HTML code must be enclosed in HTML comment tags (<!-- code -->)
        # to ensure that it will pass through this parser unaltered (in handle_comment).
        strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())
    
    #是结束一个块的 HTML 标记，象 </html>，</head>，</body> 或 </pre> 等。
    #当找到一个结束标记时，SGMLParser 将查找名为 end_tagname 的方法。如果找到，
    #SGMLParser 调用这个方法，否则它使用标记的名字来调用 unknown_endtag 。
    def unknown_endtag(self, tag):         
        # called for each end tag, e.g. for </pre>, tag will be "pre"
        # Reconstruct the original end tag.
        self.pieces.append("</%(tag)s>" % locals())
        
    #用字符的十进制或等同的十六进制来表示的转义字符，象 &#160;。当
    #找到，SGMLParser 使用十进制或等同的十六进制字符文本来调用 handle_charref 。
    def handle_charref(self, ref):         
        # called for each character reference, e.g. for "&#160;", ref will be "160"
        # Reconstruct the original character reference.
        self.pieces.append("&#%(ref)s;" % locals())

    #HTML 实体，象 &copy;。当找到，SGMLParser 使用 HTML 实体的名字来调用 handle_entityref 。
    def handle_entityref(self, ref):       
        # called for each entity reference, e.g. for "&copy;", ref will be "copy"
        # Reconstruct the original entity reference.
        self.pieces.append("&%(ref)s" % locals())
        # standard HTML entities are closed with a semicolon; other entities are not
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(";")

    #文本块。不满足其它 7 种类别的任何东西。当找到，SGMLParser 用文本来调用 handle_data。
    def handle_data(self, text):           
        # called for each block of plain text, i.e. outside of any tag and
        # not containing any character or entity references
        # Store the original text verbatim.
        #数据的处理
        self.pieces.append(text)
        
    #HTML 注释, 包括在 <!-- ... -->之间。当找到，SGMLParser 用注释内容来调用 handle_comment
    def handle_comment(self, text):        
        # called for each HTML comment, e.g. <!-- insert Javascript code here -->
        # Reconstruct the original comment.
        # It is especially important that the source document enclose client-side
        # code (like Javascript) within comments so it can pass through this
        # processor undisturbed; see comments in unknown_starttag for details.
        self.pieces.append("<!--%(text)s-->" % locals())

    #HTML 处理指令，包括在 <? ... > 之间。当找到，SGMLParser 用处理指令内容来调用 handle_pi。
    def handle_pi(self, text):             
        # called for each processing instruction, e.g. <?instruction>
        # Reconstruct original processing instruction.
        self.pieces.append("<?%(text)s>" % locals())

    #HTML 声明，如 DOCTYPE，包括在 <! ... >之间。当找到，SGMLParser 用声明内容来调用 handle_decl
    def handle_decl(self, text):
        # called for the DOCTYPE, if present, e.g.
        # <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        #     "http://www.w3.org/TR/html4/loose.dtd">
        # Reconstruct original DOCTYPE
        self.pieces.append("<!%(text)s>" % locals())

    def output(self):              
        """Return processed HTML as a single string"""
        return "".join(self.pieces)

