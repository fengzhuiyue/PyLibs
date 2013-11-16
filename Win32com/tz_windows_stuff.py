#!/usr/bin/python

# tz_windows_stuff.py
#       --copyright--                   Copyright 2009 (C) Tranzoa, Co. All rights reserved.    Warranty: You're free and on your own here. This code is not necessarily up-to-date or of public quality.
#       --url--                         https://www.tranzoa.net/tzpython/
#       --email--                       pycode is the name to send to. tranzoa.com is the place to send to.
#       --bodstamps--
#       March 30, 2009          bar
#       April 3, 2009           bar     get_mouse_left_up()
#       April 11, 2009          bar     able to run without exceptions on non-windows box
#       April 30, 2009          bar     print all the names
#       May 6, 2009             bar     de-win32ui this module
#       May 7, 2009             bar     de-console-app it
#                                       move_a_window_to_lower_rite()
#       May 8, 2009             bar     needed param
#                                       strip the window names
#       May 10, 2009            bar     xy_inside()
#       May 12, 2009            bar     comment
#       May 15, 2009            bar     make find_window able to find a window by name, too. not just class
#                                       ShowWindow()
#       May 16, 2009            bar     routine name changes
#       May 20, 2009            bar     comment for future grep use
#                                       futz with wx and the mouse (getting xy and left button work)
#                                       enum windows can use an external program
#                                       and that program can be used to move windows
#                                       don't know how to automate mouse output though (see the web app that snapshots your web page on lots of different browsers?)
#       May 21, 2009            bar     work out the python-xlib / X-windows versions of most everything that wmctrl can do for us - in """string""" comment
#       May 23, 2009            bar     be compatible with older code
#       June 3, 2009            bar     split a routine so that random movement can be limited on the window sides
#                                       and provide limit helper routines
#                                       provide some caller control over random mouse movement speed
#       September 4, 2009       bar     fix set_random_xy to not hang on windows in negative screen locations (but it's not right)
#                                       default x and y to zero to metrics conversion routines
#       October 22, 2009        bar     fool with the commented xwin code
#       February 22, 2010       bar     put some X stuff in
#       February 25, 2010       bar     more -xy window dragging
#       October 7, 2010         bar     able to use some of a_mouse under X using wx
#       October 9, 2010         bar     comment about setting mouse location in wx win.WarpPointer()  (wx.WarpPointer() does not exist as of version 2.8.11)
#       --eodstamps--
##      \file
#
#
#       Buncha special code for Windows.
#
#

import  re
import  random
import  sys
import  time

try     :
    raise ImportError
    import  wx
except ImportError :
    wx  = None

try     :
    import  pywintypes
    import  win32api
    import  win32con
    import  win32gui

    # if  'tz_wx_widgets' in globals() :
    #    import  wx
    # else :
    #    import  win32ui                         # May 6, 2009 I've not found how to use py2exe with this thing. It's needed here for FindWindow().
    from    ctypes          import windll, c_wchar_p
    from    ctypes.wintypes import LPCSTR
    user32  = windll.user32
except ( ImportError, NameError ) :
    user32  = None


try     :
    try     :
        raise ImportError
        import  wx
    except ImportError :
        wx  = None

    from    Xlib            import  X, display, XK
    import  Xlib.ext.xtest  as      xtest
    import  Xlib.error
    import  Xlib.Xutil
    try             :
        xdisplay    = display.Display()
    except Xlib.error.DisplayNameError :
        X           = None
        pass
    pass
except ( ImportError, NameError ) :
    X               = None


import  tzlib


CLASS_NAME              = "CLASS: "
TEXT_NAME               = "TEXT:  "

TASK_SWITCH_WIN_NAME    = "TASK_SWITCH"         # special name we use to kick out when the guy hits Alt Tab
CRASH_WINDOW_NAME       = "CRASH_WINDOW"        # special name we use to kick out when a new debug window pops (optimizes the regx search for the debug window)


def get_windows(pw = None) :
    wa  = []

    if  user32  :
        def show_win(h, v) :
            wa.append(h)

            return(True)

        """ os.system("wmctrl -l") ; # can be used to move and size windows, too. """


        if  pw :
            win32gui.EnumChildWindows(pw, show_win, wa)
        else :
            win32gui.EnumWindows(         show_win, wa)
        pass

    elif X  :
        sc  = xdisplay.screen()
        pw  = pw or sc.root


        def add_win(w) :
            for w in w.query_tree().children :
                wt  = w.query_tree()
                ca  = wt.children               # note: wt.parent is the parent window
                if  ca :
                    c   = ca[0]
                    if  c.get_wm_name() :
                        wa.append(c)
                    pass
                pass
            pass

        add_win(pw)

    return([ h for h in wa ])



def print_windows(wa) :
    """ Print the class names of the windows in the given list of window handles. """

    for h in wa :
        try :
            if  user32  :
                print "hwnd", h, "cn", win32gui.GetClassName(h)
            elif X      :
                print "w", h, "cn", h.get_wm_class(), repr(h.get_wm_name())
            pass
        except :
            # print
            pass
        pass
    pass



def get_window_names(pw = None) :
    """
        Get a list of all top level windows.

        \returns
            Dictionary of window (int) handles or refs keyed by class and name and such.
    """
    nms = {}
    while True :
        try :
            for h in get_windows(pw) :
                try :
                    if  user32 :
                        cn                  = win32gui.GetClassName(h).strip()
                        tn                  = win32gui.GetWindowText(h).strip()
                    elif X                  :
                        print h
                        cn                  = str(h.get_wm_class()).strip()
                        print cn
                        tn                  = h.get_wm_name().strip()
                        print tn
                    nms[cn]                 = h
                    nms[tn]                 = h
                    nms[CLASS_NAME + cn]    = h
                    nms[TEXT_NAME  + tn]    = h
                except pywintypes.error, ValueError :
                    pass
                except :
                    # print "not pywintypes.error"                              # try to find what that bad trace/exception is
                    e   = sys.exc_info()
                    if  str(e).find('pywintypes') < 0 :                         # !!!! find out what the except value is.
                        # print "raising", e[0]
                        raise
                    pass
                pass

            break

        except :
            continue

            #
            #       Run on Vista on faster PC and this will happen now and then.
            #
            print
            print
            print
            print "Got exception in win32gui.Enum...Windows(). Re-trying..."
            tzlib.print_exception()
            print
            print
            print
            pass
        pass

    return(nms)


def get_window_changes(wd, silent_names = None) :
    """
        Return three dictionaries of new, gone, current windows given a dictionary of top-level windows.

        Don't include in the 'new' and 'gone' lists any windows whose name/classes end in any name in the list (or dictionary keys) of 'silent_names'.

        \returns
            List of 'new' windows.
        \returns
            List of 'gone' windows - those that have gone away.
        \returns
            Current list of windows.
    """

    try :
        silent_names    = silent_names.keys()
    except AttributeError :
        silent_names    = silent_names or []

    gone_wd = {}
    new_wd  = {}

    was     = get_window_names()
    for n in wd.keys()  :
        if  n not in was :
            fnd         = None
            for ign in silent_names :
                if  n.endswith(ign) :
                    fnd             = n
            if  (not fnd) and   (n != CRASH_WINDOW_NAME) and (n != TASK_SWITCH_WIN_NAME) :
                gone_wd[n]          = wd[n]
            pass
        pass

    tv  = dv    = None
    for n in was.keys() :
        if  n not in wd :
            if  re.search(r"Microsoft.*Debug\s*Library", n) or re.search(r"OfficeWatson", n) :
                dv  = was[n]
            if  re.search(r"PreviewCtl",                 n) or re.search(r"TaskSwitch",   n) :
                tv  = was[n]
            fnd = None
            for ign in silent_names :
                if  n.endswith(ign) :
                    fnd             = n
            if  not fnd             :
                new_wd[n]           = was[n]
            pass
        pass
    if  dv != None :
        was[CRASH_WINDOW_NAME]      = dv
    if  tv != None :
        was[TASK_SWITCH_WIN_NAME]   = tv

    return(was, gone_wd, new_wd)


def show_window_changes(wd, silent_names = None) :
    """
        Print any changes to the given dictionary of top-level windows to the current dictionary.

        Don't print anything about any windows whose name/classes end in any name in the list (or dictionary keys) of 'silent_names'.

        \returns
            New, current dictionary of window handles from get_window_names().
    """

    ( was, gone_wd, new_wd )    = get_window_changes(wd, silent_names)
    for n in gone_wd    :
        print "Window gone", n
    for n in new_wd     :
        print "New window",  n

    return(was)





def win_pos_str(w) :
    """ Get a string with the window handle's top, bottom, left, right, width and height.

        \return
            printable string
    """
    if  not w   :
        return("NO WINDOW")

    # print type(w), w
    if  user32  :
        if  type(w) == type(1) :
            ( left, top, rite, bot )    = win32gui.GetWindowRect(w)
        else    :
            ( left, top, rite, bot )    = w.GetWindowRect()
        pass
    elif X      :
        g       = w.get_geometry()
        left    = g.x
        rite    = left + g.width
        top     = g.y
        bot     = top  + g.height

    return("x=%i y=%i r=%i b=%i w=%i h=%i" % ( left, top, rite, bot, rite - left, bot - top) )



class   a_window(object) :
    """ win32ui doesn't make it to a py2exe file, so we'll fake it for what we need. """

    def __init__(me, h) :
        me.h    = h

    def GetWindowRect(me) :
        if  user32 :
            return(win32gui.GetWindowRect(me.h))
        elif X :
            g           = me.h.get_geometry()
            return( ( g.x, g.y, g.x + g.width, g.y + g.height) )
        return( ( 0, 0, 0, 0 ) )


    def GetClassName(me) :
        if  user32 :
            return(win32gui.GetClassName(me.h))
        elif X :
            return(str(me.h.get_wm_class()))
        return("")

    def GetWindowText(me) :
        if  user32 :
            return(win32gui.GetWindowText(me.h))
        elif X :
            return(str(me.h.get_wm_name()))
        return("")

    def GetClientRect(me) :
        if  user32 :
            return(win32gui.GetClientRect(me.h))
        elif X :
            return(me.GetWindowRect())
        return( ( 0, 0, 0, 0 ) )

    def IsWindowVisible(me) :
        return(win32gui.IsWindowVisible(me.h))

    def SetWindowPos(me, p, rect, i) :
        if  user32  :

            return(win32gui.SetWindowPos(me.h, p, rect[0], rect[1], rect[2], rect[3], i))

        if  X :
            ec  = Xlib.error.CatchError()
            x   = rect[0]
            y   = rect[1]
            w   = rect[2] - rect[0]
            h   = rect[3] - rect[1]
            if  (x < 0) or (y < 0) :
                alt_k   = xdisplay.keysym_to_keycode(Xlib.XK.XK_Alt_R)

                me.h.configure(x = 0, y = 0, width = max(60, w), height = max(60, h), onerror = ec)
                xdisplay.sync()

                do_mouse_event('m', 50, 50)                                     # !!!! get the current position and restore it

                xdisplay.xtest_fake_input(Xlib.X.KeyPress, alt_k)
                xdisplay.flush()

                do_mouse_event('d', 50, 50)

                do_mouse_event('m', 10, 10)                                     # moves the window off-screen so it can be moved other places off screen

                do_mouse_event('u', 10, 10)

                xdisplay.xtest_fake_input(Xlib.X.KeyRelease, alt_k)
                xdisplay.flush()

            me.h.configure(x = x, y = y, width = w, height = h, onerror = ec)
            xdisplay.sync()
            if  not ec.get_error() :

                return(True)

            pass

        return(False)

    def SetForegroundWindow(me) :
        if  user32 :
            return(win32gui.SetForegroundWindow(me.h))          # give this window the focus
        elif X :
            ec  = Xlib.error.CatchError()
            me.h.set_input_focus(X.RevertToParent, X.CurrentTime, onerror = ec)
            display.Display().sync()
            if  ec.get_error() :
                return(False)
            return(me)
        return(None)

    def ShowWindow(me, how = None) :
        if  user32  :
            if  how    == None :
                how     = win32con.SW_SHOW

            if  type(how) == type(True) :
                how     = (how and win32con.SW_SHOW) or win32con.SW_HIDE
            win32gui.ShowWindow(me.h, how)

        elif X :

            if  how    == None :
                how     = True

            if  how    == True :
                me.h.set_wm_state(state = Xlib.Xutil.NormalState)                       # ????
            elif how   == False :
                me.h.set_wm_state(state = Xlib.Xutil.IconicState, icon = 0)             # !!!! no
            elif not how :
                me.h.unmap()
            else        :
                me.h.map()

            display.Display().sync()
        pass

    pass        # a_window




def get_foreground_window() :
    w   = user32.GetForegroundWindow()
    if  w :
        return(a_window(w))

    return(None)


def move_a_window_to_lower_rite(win) :
    ( dleft, dtop, drite, dbot )    = get_desktop_window_bounds()

    ( left, top, rite, bot )        = win.GetWindowRect()

    w   =   rite    - left
    h   =   bot     - top
    nx  =   drite   - w
    ny  =   dbot    - h
    win.SetWindowPos(win32con.HWND_TOP, ( nx, ny, w, h ), 0)

    return(nx, ny, w, h)






def find_window(name) :
    """
        Find the window with the given class or "name" (text).

        \returns
            PyWnd for the window.
    """

    if  name.startswith(CLASS_NAME) :
        name    = name[len(CLASS_NAME):]
    if  name.startswith(TEXT_NAME) :
        name    = name[len(TEXT_NAME):]

    w           = None

    if  user32  :
        try :
            w       = user32.FindWindowA(LPCSTR(name), 0)
            if  w   :
                w   = a_window(w)
            else :
                w   = None
                w       = user32.FindWindowA(0, LPCSTR(name))
                if  w   :
                    w   = a_window(w)
                else :
                    w   = None
                pass
            pass
        except      :
            w       = None
        pass

    elif X :
        wa          = get_windows()
        for ww in wa :
            if  name == ww.get_wm_name() :
                w   = ww
                break
            pass

        if  not w   :
            for ww in wa :
                cl      = ww.get_wm_class()
                if  name in cl :
                    w   = ww
                    break
                pass
            pass
        pass

    return(w)



class a_window_metrics(object)  :
    """
        A handy object that has various bits of information about a window (either handle or PyWnd).
    """

    def __init__(me, w = None)  :
        me.class_name           = ""
        if  not w :
            w                   = win32gui.GetDesktopWindow()
        if  isinstance(w, basestring) :
            me.class_name       = w
            w                   = find_window(w)

        me.win                  = w
        if  type(w) == type(1)  :
            ( me.left,  me.top,  me.rite,  me.bot  )    = win32gui.GetWindowRect(w)
            ( me.cleft, me.ctop, me.crite, me.cbot )    = win32gui.GetClientRect(w)
            me.visible                                  = win32gui.IsWindowVisible(w)
            me.text                                     = win32gui.GetWindowText(w)
            me.class_name                               = win32gui.GetClassName(w)
        else :
            ( me.left,  me.top,  me.rite,  me.bot  )    = w.GetWindowRect()
            ( me.cleft, me.ctop, me.crite, me.cbot )    = w.GetClientRect()
            me.visible                                  = w.IsWindowVisible()
            me.text                                     = w.GetWindowText()

        me.cx                   = me.cleft
        me.cy                   = me.ctop
        me.cw                   = me.crite - me.cleft
        me.ch                   = me.cbot  - me.ctop

        me.x                    = me.left
        me.y                    = me.top
        me.w                    = me.rite  - me.left
        me.h                    = me.bot   - me.top

        me.border_width         = (me.w - me.cw) / 2                    # scroll bar can take room !!!!
        me.top_bar_hite         = (me.h - me.ch) - (me.w - me.cw)


    def set_xy(me, x, y) :
        me.x    = me.left       = x
        me.rite = me.x + me.w
        me.y    = me.top        = y
        me.bot  = me.y + me.h



    def get_screen_xy(me, x = 0, y = 0) :                               # legacy routine
        return(me.window_to_screen_xy(x, y))

    def get_window_xy(me, x = 0, y = 0) :                               # legacy routine
        return(me.screen_to_window_xy(x, y))


    def screen_to_window_xy(me, x = 0, y = 0) :
        return(x - me.x, y - me.y)

    def window_to_screen_xy(me, x = 0, y = 0) :
        return(x + me.x, y + me.y)


    def screen_to_client_xy(me, x = 0, y = 0) :
        return(x - me.x - me.border_width, y - me.y - me.border_width - me.top_bar_hite)

    def client_to_screen_xy(me, x = 0, y = 0) :
        return(x + me.border_width + me.x, y + me.border_width + me.top_bar_hite + me.y)


    def screen_xy_inside(me, x = 0, y = 0) :
        return((me.left <= x < me.rite) and (me.top <= y < me.bot))

    def screen_xy_inside_client(me, x = 0, y = 0) :
        return((me.left + me.border_width <= x < me.rite - me.border_width) and (me.top + me.border_width + me.top_bar_hite <= y < me.bot - me.border_width))


    def __cmp__(me, om) :
        i   = cmp(me.y, om.y)
        if  i :
            return(i)
        i   = cmp(me.x, om.x)
        if  i :
            return(i)
        i   = cmp(me.h, om.h)
        if  i :
            return(i)
        i   = cmp(me.w, om.w)
        if  i :
            return(i)
        i   = cmp(me.class_name, om.class_name)
        if  i :
            return(i)
        i   = cmp(me.text, om.text)
        if  i :
            return(i)

        return(0)

    def __str__(me) :
        return("x=%d y=%d w=%d h=%d b=%d t=%d" % ( me.x, me.y, me.w, me.h, me.border_width, me.top_bar_hite ))

    pass                        # a_window_metrics



def get_stable_window_metrics(wname) :
    """
        Get a_window_metrics for the given, name/classed window.

        \returns
            a_window_metrics object.
    """

    wm      = a_window_metrics(wname)
    while True :
        nsw = a_window_metrics(wm.win)
        if  nsw    == wm :                              # has the window settled down to where it's going to be?
            break
        wm  = nsw
        time.sleep(0.1)

    return(wm)



def x_close_window(w, ms = None) :
    """
        Using the given a_mouse, click on the given visible window's X close button.

        \returns
            True if the window was clicked.
        \returns
            False if the window was not visible or if it could not be found.
    """

    try :
        wm  = a_window_metrics(w)
        if  wm.visible :
            ms  = ms or a_mouse()
            x   = wm.rite - wm.border_width - 10
            y   = wm.top + wm.border_width + (wm.top_bar_hite / 2)
            # print x, y, wm.rite, wm.top, wm.border_width, wm.top_bar_hite
            ms.click_on(x, y)                                       # hit the X button

            return(True)
        pass
    except pywintypes.error :
        pass

    return(False)





def get_desktop_window_bounds() :
    """
        Get the bounds of the desktop window.

        \returns
            (left,top,right,bottom) pixel locations.
    """

    if wx :
        dleft   = 0
        dtop    = 0
        sz      = wx.GetDisplaySize()
        drite   = sz.GetWidth()
        dbot    = sz.GetHeight()
    elif X      :
        sc      = xdisplay.screen()
        return(0, 0, sc.width_in_pixels, sc.height_in_pixels)
    else        :
        ( dleft, dtop, drite, dbot )    = win32gui.GetWindowRect(win32gui.GetDesktopWindow())

    return(dleft, dtop, drite, dbot)





def mmx(x) :
    """
        Translate the given X pixel value to a mouse position.
    """

    ( dleft, dtop, drite, dbot )    = get_desktop_window_bounds()

    d                               = drite - dleft

    mx                              = int((x * 65535) / d)
    while int((mx * d) / 0x10000)   < x :
        if  x < dleft               :
            break
        mx                         += 1
        if  x >= drite              :
            break
        pass

    return(mx)


def mmy(y) :
    """
        Translate the given Y pixel value to a mouse position.
    """

    ( dleft, dtop, drite, dbot )    = get_desktop_window_bounds()

    d                               = dbot  - dtop

    my                              = int((y * 65535) / d)
    while int((my * d) / 0x10000)   < y :
        if  y < dtop                :
            break
        my                         += 1
        if  y >= dbot               :
            break
        pass

    return(my)



"""
    #
    #       http://python-xlib.sourceforge.net/doc/html/python-xlib_toc.html
    #       Search 'python' and the function names for examples or help.
    #
    #       http://library.gnome.org/devel/wm-spec/
    #
    #       http://www.semicomplete.com/projects/xdotool/
    #

    import  re

    from    Xlib            import  X, display
    import  Xlib.ext.xtest  as      xtest
    import  Xlib.error
    import  Xlib.Xutil


    ds          = display.Display()

    def goto_xy(x, y) :
        xtest.fake_input(ds, X.MotionNotify, x = x, y = y)
        ds.flush()



    LEFT_BUTTON = 1
    MID_BUTTON  = 2
    RITE_BUTTON = 3

    def left_down(down = True, button = LEFT_BUTTON) :

        dv      = 0
        du      = X.ButtonPress
        if  not down :
            dv  = 5
            du  = X.ButtonRelease

        button  = button or LEFT_BUTTON

        ds.xtest_fake_input(du, button, dv)
        ds.flush()                                                              # gets things going, but does not go synchronous, I presume


    if  False :
        goto_xy(1000, 250)
        left_down(True,  RITE_BUTTON)
        left_down(False, RITE_BUTTON)

    find_wind   = "AnalogClock" # "System Monitorx"

    find_wind   = find_wind.strip().lower()

    print "ds version", ds.xtest_get_version(0, 0), xtest.get_version(ds, 0, 0)

    sc  = ds.screen()
    print ds.get_display_name(), sc.width_in_pixels, sc.height_in_pixels, ds.screen_count(), ds.get_default_screen()
    tw  = sc.root
    wa  = tw.query_tree()

    p       = tw.get_full_property(ds.get_atom('_NET_NUMBER_OF_DESKTOPS'), ds.get_atom('CARDINAL'))
    print p.value[0], "desktops. Currently",
    p       = tw.get_full_property(ds.get_atom('_NET_CURRENT_DESKTOP'), ds.get_atom('CARDINAL'))
    print p.value[0]


    ds.force_screen_saver(X.ScreenSaverReset)           # X.ScreenSaverActive the screen saver is activated. If it is X.ScreenSaverReset

    win = None
    for w in wa.children :
        wt  = w.query_tree()
        ca  = wt.children
        if  ca :
            c   = ca[0]
            if  c.get_wm_name() :                                               # does the 1st child window have a title (which is what we see on the title bar)?

                # print wt.root, wt.parent

                if  c.get_wm_name().lower().strip() == find_wind :
                    p   =      c.get_property(ds.get_atom('_NET_WM_DESKTOP'), ds.get_atom('CARDINAL'), 0, 10)
                    print "p", p.value, p.bytes_after

                p       = c.get_full_property(ds.get_atom('_NET_WM_DESKTOP'), ds.get_atom('CARDINAL'))
                if  not p :
                    print "nonet"
                    p   = c.get_full_property(ds.get_atom('_WIN_WORKSPACE'),  ds.get_atom('CARDINAL'))
                if  not p :
                    p   = ""
                else    :
                    p   = p.value[0]
                    if  p & 0x80000000L :
                        p = (~p + 1) & 0xFFFFffffL
                        p = -p
                    p   = str(int(p))

                g       = w.get_geometry()

                st      = c.get_wm_state().state
                if  st == Xlib.Xutil.WithdrawnState :
                    st  = "WithdrawnState"
                elif st == Xlib.Xutil.NormalState   :
                    st  = "NormalState"
                elif st == Xlib.Xutil.IconicState   :                           # state of windows on other desktops, too
                    st  = "IconicState"
                else    :
                    st  = "Unknown:" + str(st)

                print "class[%s] title[%s] screen=%s x=%d y=%d w=%d h=%d state=%s" % ( str(c.get_wm_class()), str(c.get_wm_name()), p, g.x, g.y, g.width, g.height, st )

                if  c.get_wm_name() and (c.get_wm_name().lower().strip() == find_wind) :
                    win = w
                    wc  = c
                pass
            pass
        pass


    if  win :
        # import  array

        # print "\n".join([ p for p in dir(win) if True or re.search(r"prop", str(p)) ] )

        ec  = Xlib.error.CatchError()

        # aa  = array.array('I', ( 0xffffFFFF, ))
        # print "aa", aa

        # st  = wc.get_wm_state()
        # print "state", "\n".join(dir(st)), st
        # print

        # win.change_property(ds.get_atom('_NET_WM_DESKTOP'), ds.get_atom('CARDINAL'), 32, aa)
        # wc. change_property(ds.get_atom('_NET_WM_DESKTOP'), ds.get_atom('CARDINAL'), 32, aa, onerror = ec)

        # bb  = array.array('I', ( 0, ))
        # wc.change_property(ds.get_atom('_NET_WM_STATES_STICKY'), ds.get_atom('CARDINAL'), 32, bb, onerror = ec)

        # win.unmap()
        # win.set_wm_state(state = Xlib.Xutil.IconicState, icon = 0)            # no!

        # wc.unmap()
        # wc.set_wm_state( state = Xlib.Xutil.IconicState, icon = 0)            # doesn't work
        # wc.map()                                                              # we won't be be able to find it if we leave it unmapped

        #
        #   xdotool code helped here!
        #
        dsk_num = 0xffffFFFF        # special value for "Always on visible workspace" - otherwise 0.. for specific workspaces
        evt     = Xlib.protocol.event.ClientMessage(display = ds, window = wc, client_type = ds.get_atom('_NET_WM_DESKTOP'), data = ( 32, ( 0xffffFFFF, 2, 0, 0, 0 ) ) )

        # print "Event", "\n".join(dir(evt)), evt
        # print
        # print "win", "\n".join(dir(wc)), win
        # print

        ds.send_event(tw, evt, event_mask = X.SubstructureNotifyMask | X.SubstructureRedirectMask, onerror = ec)



        ds.sync()                                                               # wait for any errors
        if  ec.get_error() :
            print "Did not set property!"


        print "sticky",  wc.get_full_property(ds.get_atom('_NET_WM_STATES_STICKY'), ds.get_atom('CARDINAL')).value
        print "desktop", wc.get_full_property(ds.get_atom('_NET_WM_DESKTOP'), ds.get_atom('CARDINAL')).value


        if  0 :
            print "focusing and moving and sizing", win, wc

            ec  = Xlib.error.CatchError()

            win.set_input_focus(X.RevertToParent, X.CurrentTime, onerror = ec)      # or wc can also get the focus

            wc.configure(x = 100, width = 1000,                  onerror = ec)      # this works even if the window is on another desktop

            ds.sync()                                                               # wait for any errors
            if  ec.get_error() :
                print "Did not focus!"                                              # fails focus if the window is on another desktop
            pass
        pass

    pass
"""





def do_mouse_event(e, x, y) :
    if  user32  :
        if  isinstance(e, basestring) :
            #                                               note: unfortunately, wx.GetMouseState().SetX/Y() and SetLeftDown(tf) don't work - under win32 anyway
            if      e  == 'm' :
                    e   = win32con.MOUSEEVENTF_MOVE
            elif    e  == 'd' :
                    e   = win32con.MOUSEEVENTF_LEFTDOWN
            else              :
                    e   = win32con.MOUSEEVENTF_LEFTUP
            pass

        win32api.mouse_event(e  + win32con.MOUSEEVENTF_ABSOLUTE, mmx(x),  mmy(y),  0, 0)

    elif X :

        def goto_xy(x, y) :
            xtest.fake_input(xdisplay, X.MotionNotify, x = x, y = y)
            xdisplay.flush()
            xdisplay.sync()


        LEFT_BUTTON = 1
        MID_BUTTON  = 2
        RITE_BUTTON = 3

        def left_down(down = True, button = LEFT_BUTTON) :

            dv      = 0
            du      = X.ButtonPress
            if  not down :
                dv  = 5
                du  = X.ButtonRelease

            button  = button or LEFT_BUTTON

            xdisplay.xtest_fake_input(du, button, dv)
            xdisplay.flush()                                                                # gets things going, but does not go synchronous, I presume
            xdisplay.sync()

        def left_up(button = LEFT_BUTTON) :
            left_down(False, button)

        goto_xy(x, y)           # !!!! do mmx mmy

        if      e  == 'm' :
            pass
        elif    e  == 'd' :
            left_down()
        else              :
            left_up()
        pass

    elif wx :
        # setting mouse location: window.WarpPointer() - it's in terms of window location (so if the Window is a scrolled window, xy may need to be CalcScrolledPosition()'d
        pass

    pass



class   a_mouse(object) :
    """ An object for doing things directly with the mouse. """


    SPEED   = 5


    def __init__(me) :
        ( me.dleft, me.dtop, me.drite, me.dbot )    = get_desktop_window_bounds()

        me._speed   = me.SPEED
        me.lup      = True
        me.learn_current_xy()
        me.be_still()
        me.be_a_slacker()



    @classmethod
    def get_mouse_xy(me) :
        if  wx          :
            ( x, y )    = wx.GetMousePosition()
        elif X          :
            data        = xdisplay.screen().root.query_pointer()._data
            x           = data["root_x"]
            y           = data["root_y"]
        else            :
            ( x, y )    = win32gui.GetCursorPos()

        return(x, y)


    @classmethod
    def get_mouse_left_up(me) :
        if  wx          :
            return(not wx.GetMouseState().LeftDown())
        if  X           :
            data        = xdisplay.screen().root.query_pointer()._data
            return(not (data["mask"] & 256))                                # middle button is 512, rite button is 1024

        return(win32api.GetAsyncKeyState(win32con.VK_LBUTTON) == 0)


    def me_xy(me, x = None, y = None) :
        if  x  == None :
            x   = me.x
        if  y  == None :
            y   = me.y

        return(x, y)



    def speed(me, sp    = None) :
        ov              = me._speed

        if  sp  :
            me._speed   = sp

        return(ov)



    def force_to_xy(me, x = None, y = None) :
        ( dleft, dtop, drite, dbot )    = get_desktop_window_bounds()

        ( x, y )                        = me.me_xy(x, y)
        while True :
            do_mouse_event('m', x, y)
            ( mx, my )    = me.get_mouse_xy()
            if  (mx == x) and (my == y) :
                break
            time.sleep(0.01)
            if  (not (dleft <= x < drite)) or (not (dtop <= y < dbot)) :
                break
            pass
        pass



    def left_push(me, x = None, y = None) :
        ( x, y )    = me.me_xy(x, y)
        me.force_to_xy(x, y)
        me.lup  = False
        do_mouse_event('d', x, y)


    def left_release(me,       x = None, y = None) :
        ( x, y )    = me.me_xy(x, y)
        me.force_to_xy(        x, y)
        do_mouse_event('u',    x, y)
        me.lup  = True


    def get_left_up(me) :
        return(me.lup)


    def get_xy(me) :
        return(me.x, me.y)


    def insure_up(me)   :
        if  not me.lup  :
            me.lup      = True
            ( mx, my )  = me.get_mouse_xy()
            do_mouse_event('u', mx, my)

            return(False)

        return(True)


    def left_click(me,  x = None, y = None) :
        me.left_push(   x, y)
        me.left_release(x, y)


    def click_on(me, x  = None, y = None) :
        ( mx, my )      = me.get_mouse_xy()
        me.left_click(       x,  y)
        do_mouse_event('m', mx, my)


    def goto(me, x  = None, y = None) :
        ( x, y )    = me.me_xy(x, y)
        me.x        = x
        me.y        = y
        do_mouse_event('m', x, y)


    def learn_current_xy(me) :
        ( me.x, me.y )  = me.get_mouse_xy()


    def set_random_xy(me, win)  :
        if  win :
            if  not isinstance(win, a_window) :
                ( left, top)    = win.client_to_screen_xy(0, 0)
                ( rite, bot)    = win.client_to_screen_xy(win.cw, win.ch)
            else                :
                ( left, top, rite, bot )    = win.GetWindowRect()

            if  me.x    < left :
                me.dx  += 1
                me.dx   = max(min(me.dx, me._speed), -me._speed)
            if  me.x    > rite :
                me.dx  -= 1
                me.dx   = max(min(me.dx, me._speed), -me._speed)
            if  me.y    < top :
                me.dy  += 1
                me.dy   = max(min(me.dy, me._speed), -me._speed)
            if  me.y    > bot :
                me.dy  -= 1
                me.dy   = max(min(me.dy, me._speed), -me._speed)
            pass

        inc     = 2

        xb      = -inc * 2
        if  me.gx != None :
            if  abs(me.x + me.dx - me.gx) > abs(me.x - me.gx) :
                if  me.dx > 0 :
                    xb -= inc
                else :
                    xb += inc
                pass
            pass
        yb      = -inc * 2
        if  me.gy != None :
            if  abs(me.y + me.dy - me.gy) > abs(me.y - me.gy) :
                if  me.dy > 0 :
                    yb -= inc
                else :
                    yb += inc
                pass
            pass

        me.dx  += random.randint(xb, xb + 4 * inc)
        me.dy  += random.randint(yb, yb + 4 * inc)

        #
        #   Move, but don't go outside the display
        #   !!!! does not work correctly with 2nd, negative desktop as our get_desktop_window_bounds only gets the primary display rectangle
        #
        x               = me.x + me.dx
        if  x           < me.dleft :
            if  me.dx   < 0 :
                me.dx   = -me.dx
            me.dx      /= 2
        elif x         >= me.drite :
            if  me.dx   > 0 :
                me.dx   = -me.dx
            me.dx      /= 2
        else            :
            me.x        = x
        pass

        y               = me.y + me.dy
        if  y           < me.dtop :
            if  me.dy   < 0 :
                me.dy   = -me.dy
            me.dy      /= 2
        elif y         >= me.dbot :
            if  me.dy   > 0 :
                me.dy   = -me.dy
            me.dy      /= 2
        else            :
            me.y        = y
        pass

        # print me.x, me.dx, me.y, me.dy


    def random_move(me, win) :
        me.set_random_xy(win)
        me.goto()


    def set_inside_west(me) :
        if  me.x    < 0 :
            me.x    = 0
            me.dx   = max(me.dx, 0)
        pass

    def set_inside_east(me) :
        if  me.x   >= me.drite :
            me.x    = me.drite - 1
            me.dx   = min(me.dx, 0)
        pass

    def set_inside_top(me) :
        if  me.y    < 0 :
            me.y    = 0
            me.dy   = max(me.dy, 0)
        pass

    def set_inside_bottom(me) :
        if  me.y   >= me.dbot :
            me.y    = me.dbot - 1
            me.dy   = min(me.dy, 0)
        pass


    def be_still(me) :
        me.dx   = me.dy = 0


    def be_unsteady(me) :
        me.dx   = random.randint(-me._speed, me._speed)
        me.dy   = random.randint(-me._speed, me._speed)


    def be_a_slacker(me) :
        me.gx   = me.gy = None


    def set_goal(me, x  = None, y = None) :
        me.gx   = x
        me.gy   = y


    pass        # a_mouse



"""
    wx.GetKeyState(k)
"""



def turn_off_caps_lock() :
    """ Turn off the caps lock key. """

    if  win32api.GetKeyState(win32con.VK_CAPITAL) :
        win32api.keybd_event(win32con.VK_CAPITAL, 0x3a, win32con.KEYEVENTF_EXTENDEDKEY                           , 0)
        win32api.keybd_event(win32con.VK_CAPITAL, 0x3a, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
    pass



def alt_pressed() :
    """ Is an ALT key pressed?

        \returns
            True if an ALT key is pressed.
        \returns
            False if no ALT key is pressed.
    """

    if  False :
        kys = [
                [ win32con.VK_LBUTTON, 'LBUTTON' ],
                [ win32con.VK_RBUTTON, 'RBUTTON' ],
                [ win32con.VK_CANCEL, 'CANCEL' ],
                [ win32con.VK_MBUTTON, 'MBUTTON' ],
                [ win32con.VK_BACK, 'BACK' ],
                [ win32con.VK_TAB, 'TAB' ],
                [ win32con.VK_CLEAR, 'CLEAR' ],
                [ win32con.VK_RETURN, 'RETURN' ],
                [ win32con.VK_SHIFT, 'SHIFT' ],
                [ win32con.VK_CONTROL, 'CONTROL' ],
                [ win32con.VK_MENU, 'MENU' ],
                [ win32con.VK_PAUSE, 'PAUSE' ],
                [ win32con.VK_CAPITAL, 'CAPITAL' ],
                [ win32con.VK_KANA, 'KANA' ],
                [ win32con.VK_HANGEUL, 'HANGEUL' ],
                [ win32con.VK_HANGUL, 'HANGUL' ],
                [ win32con.VK_JUNJA, 'JUNJA' ],
                [ win32con.VK_FINAL, 'FINAL' ],
                [ win32con.VK_HANJA, 'HANJA' ],
                [ win32con.VK_KANJI, 'KANJI' ],
                [ win32con.VK_ESCAPE, 'ESCAPE' ],
                [ win32con.VK_CONVERT, 'CONVERT' ],
                [ win32con.VK_NONCONVERT, 'NONCONVERT' ],
                [ win32con.VK_ACCEPT, 'ACCEPT' ],
                [ win32con.VK_MODECHANGE, 'MODECHANGE' ],
                [ win32con.VK_SPACE, 'SPACE' ],
                [ win32con.VK_PRIOR, 'PRIOR' ],
                [ win32con.VK_NEXT, 'NEXT' ],
                [ win32con.VK_END, 'END' ],
                [ win32con.VK_HOME, 'HOME' ],
                [ win32con.VK_LEFT, 'LEFT' ],
                [ win32con.VK_UP, 'UP' ],
                [ win32con.VK_RIGHT, 'RIGHT' ],
                [ win32con.VK_DOWN, 'DOWN' ],
                [ win32con.VK_SELECT, 'SELECT' ],
                [ win32con.VK_PRINT, 'PRINT' ],
                [ win32con.VK_EXECUTE, 'EXECUTE' ],
                [ win32con.VK_SNAPSHOT, 'SNAPSHOT' ],
                [ win32con.VK_INSERT, 'INSERT' ],
                [ win32con.VK_DELETE, 'DELETE' ],
                [ win32con.VK_HELP, 'HELP' ],
                [ win32con.VK_LWIN, 'LWIN' ],
                [ win32con.VK_RWIN, 'RWIN' ],
                [ win32con.VK_APPS, 'APPS' ],
                [ win32con.VK_NUMPAD0, 'NUMPAD0' ],
                [ win32con.VK_NUMPAD1, 'NUMPAD1' ],
                [ win32con.VK_NUMPAD2, 'NUMPAD2' ],
                [ win32con.VK_NUMPAD3, 'NUMPAD3' ],
                [ win32con.VK_NUMPAD4, 'NUMPAD4' ],
                [ win32con.VK_NUMPAD5, 'NUMPAD5' ],
                [ win32con.VK_NUMPAD6, 'NUMPAD6' ],
                [ win32con.VK_NUMPAD7, 'NUMPAD7' ],
                [ win32con.VK_NUMPAD8, 'NUMPAD8' ],
                [ win32con.VK_NUMPAD9, 'NUMPAD9' ],
                [ win32con.VK_MULTIPLY, 'MULTIPLY' ],
                [ win32con.VK_ADD, 'ADD' ],
                [ win32con.VK_SEPARATOR, 'SEPARATOR' ],
                [ win32con.VK_SUBTRACT, 'SUBTRACT' ],
                [ win32con.VK_DECIMAL, 'DECIMAL' ],
                [ win32con.VK_DIVIDE, 'DIVIDE' ],
                [ win32con.VK_F1, 'F1' ],
                [ win32con.VK_F2, 'F2' ],
                [ win32con.VK_F3, 'F3' ],
                [ win32con.VK_F4, 'F4' ],
                [ win32con.VK_F5, 'F5' ],
                [ win32con.VK_F6, 'F6' ],
                [ win32con.VK_F7, 'F7' ],
                [ win32con.VK_F8, 'F8' ],
                [ win32con.VK_F9, 'F9' ],
                [ win32con.VK_F10, 'F10' ],
                [ win32con.VK_F11, 'F11' ],
                [ win32con.VK_F12, 'F12' ],
                [ win32con.VK_F13, 'F13' ],
                [ win32con.VK_F14, 'F14' ],
                [ win32con.VK_F15, 'F15' ],
                [ win32con.VK_F16, 'F16' ],
                [ win32con.VK_F17, 'F17' ],
                [ win32con.VK_F18, 'F18' ],
                [ win32con.VK_F19, 'F19' ],
                [ win32con.VK_F20, 'F20' ],
                [ win32con.VK_F21, 'F21' ],
                [ win32con.VK_F22, 'F22' ],
                [ win32con.VK_F23, 'F23' ],
                [ win32con.VK_F24, 'F24' ],
                [ win32con.VK_NUMLOCK, 'NUMLOCK' ],
                [ win32con.VK_SCROLL, 'SCROLL' ],
                [ win32con.VK_LSHIFT, 'LSHIFT' ],
                [ win32con.VK_RSHIFT, 'RSHIFT' ],
                [ win32con.VK_LCONTROL, 'LCONTROL' ],
                [ win32con.VK_RCONTROL, 'RCONTROL' ],
                [ win32con.VK_LMENU, 'LMENU' ],
                [ win32con.VK_RMENU, 'RMENU' ],
                [ win32con.VK_PROCESSKEY, 'PROCESSKEY' ],
                [ win32con.VK_ATTN, 'ATTN' ],
                [ win32con.VK_CRSEL, 'CRSEL' ],
                [ win32con.VK_EXSEL, 'EXSEL' ],
                [ win32con.VK_EREOF, 'EREOF' ],
                [ win32con.VK_PLAY, 'PLAY' ],
                [ win32con.VK_ZOOM, 'ZOOM' ],
                [ win32con.VK_NONAME, 'NONAME' ],
                [ win32con.VK_PA1, 'PA1' ],
                [ win32con.VK_OEM_CLEAR, 'OEM_CLEAR' ],
                [ win32con.MOUSEEVENTF_XDOWN, 'SEEVENTF_XDOWN' ],
                [ win32con.MOUSEEVENTF_XUP, 'SEEVENTF_XUP' ],
                [ win32con.MOUSEEVENTF_WHEEL, 'SEEVENTF_WHEEL' ],
                [ win32con.VK_XBUTTON1, 'XBUTTON1' ],
                [ win32con.VK_XBUTTON2, 'XBUTTON2' ],
                [ win32con.VK_VOLUME_MUTE, 'VOLUME_MUTE' ],
                [ win32con.VK_VOLUME_DOWN, 'VOLUME_DOWN' ],
                [ win32con.VK_VOLUME_UP, 'VOLUME_UP' ],
                [ win32con.VK_MEDIA_NEXT_TRACK, 'MEDIA_NEXT_TRACK' ],
                [ win32con.VK_MEDIA_PREV_TRACK, 'MEDIA_PREV_TRACK' ],
                [ win32con.VK_MEDIA_PLAY_PAUSE, 'MEDIA_PLAY_PAUSE' ],
                [ win32con.VK_BROWSER_BACK, 'BROWSER_BACK' ],
                [ win32con.VK_BROWSER_FORWARD, 'BROWSER_FORWARD' ],
            ]
        for k in kys :
            if  win32api.GetKeyState(k[0]) :
                print k[1], win32api.GetKeyState(k[0])
            pass
        pass

    return(win32api.GetKeyState(win32con.VK_MENU) < 0)


def turn_off_alt()      :       # does not work (and should not, anyway)
    if  alt_pressed()   :
        win32api.keybd_event(win32con.VK_MENU, 0x38, win32con.KEYEVENTF_EXTENDEDKEY                           , 0)
        win32api.keybd_event(win32con.VK_MENU, 0x38, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
    pass



if  __name__ == '__main__' :
    if  user32 :
        turn_off_caps_lock()

        print_windows(get_window_names())

    pass



#
#
# eof
