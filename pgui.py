#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  client_menu.py
#  
#  Copyright 2014 notna <notna@apparat.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pygame, sys, random, tools, traceback

# Need to add client_menu.font = font in main func
# also need to add client_menu.screen = screen

WIDGET_STATE_NONE = 0
WIDGET_STATE_HOVER = 1
WIDGET_STATE_CLICKED = 2

p = pygame
KEY2TXT = {p.K_BACKSPACE:"", ## Dont need this, use e.unicode instead
           p.K_TAB:"",
           p.K_CLEAR:"",
           p.K_RETURN:"",
           p.K_PAUSE:"",
           p.K_ESCAPE:"^",
           p.K_SPACE:" ",
           p.K_EXCLAIM:"!",
           p.K_QUOTEDBL:'"',
           p.K_HASH:"#",
           p.K_DOLLAR:"$",
           p.K_AMPERSAND:"&",
           p.K_QUOTE:"'",
           p.K_LEFTPAREN:"(",
           p.K_RIGHTPAREN:")",
           p.K_ASTERISK:"*",
           p.K_PLUS:"+",
           p.K_COMMA:",",
           p.K_MINUS:"-",
           p.K_PERIOD:".",
           p.K_SLASH:"/",
           p.K_0:"0",
           p.K_1:"1",
           p.K_2:"2",
           p.K_3:"3",
           p.K_4:"4",
           p.K_5:"5",
           p.K_6:"6",
           p.K_7:"7",
           p.K_8:"8",
           p.K_9:"9",
           p.K_COLON:":",
           p.K_SEMICOLON:";",
           p.K_LESS:"<",
           p.K_EQUALS:"=",
           p.K_GREATER:">",
           p.K_QUESTION:"?",
           p.K_AT:"@",
           p.K_LEFTBRACKET:"[",
           p.K_BACKSLASH:"\\",
           p.K_RIGHTBRACKET:"]",
           p.K_CARET:"^",
           p.K_UNDERSCORE:"_",
           p.K_BACKQUOTE:"`",
           p.K_a:"a",
           p.K_b:"b",
           p.K_c:"c",
           p.K_d:"d",
           p.K_e:"e",
           p.K_f:"f",
           p.K_g:"g",
           p.K_h:"h",
           p.K_i:"i",
           p.K_j:"j",
           p.K_k:"k",
           p.K_l:"l",
           p.K_m:"m",
           p.K_n:"n",
           p.K_o:"o",
           p.K_p:"p",
           p.K_q:"q",
           p.K_r:"r",
           p.K_s:"s",
           p.K_t:"t",
           p.K_u:"u",
           p.K_v:"v",
           p.K_w:"w",
           p.K_x:"x",
           p.K_y:"y",
           p.K_z:"z",
           p.K_DELETE:"",
           p.K_KP0:"0",
           p.K_KP1:"1",
           p.K_KP2:"2",
           p.K_KP3:"3",
           p.K_KP4:"4",
           p.K_KP5:"5",
           p.K_KP6:"6",
           p.K_KP7:"7",
           p.K_KP8:"8",
           p.K_KP9:"9",
           p.K_KP_PERIOD:".",
           p.K_KP_DIVIDE:"/",
           p.K_KP_MULTIPLY:"*",
           p.K_KP_MINUS:"-",
           p.K_KP_PLUS:"+",
           p.K_KP_ENTER:"",
           p.K_KP_EQUALS:"=",
           p.K_UP:"",
           p.K_DOWN:"",
           p.K_RIGHT:"",
           p.K_LEFT:"",
           p.K_INSERT:"",
           p.K_HOME:"",
           p.K_END:"",
           p.K_PAGEUP:"",
           p.K_PAGEDOWN:"",
           p.K_F1:"",
           p.K_F2:"",
           p.K_F3:"",
           p.K_F4:"",
           p.K_F5:"",
           p.K_F6:"",
           p.K_F7:"",
           p.K_F8:"",
           p.K_F9:"",
           p.K_F10:"",
           p.K_F11:"",
           p.K_F12:"",
           p.K_F13:"",
           p.K_F14:"",
           p.K_F15:"",
           p.K_NUMLOCK:"",
           p.K_CAPSLOCK:"",
           p.K_SCROLLOCK:"",
           p.K_RSHIFT:"",
           p.K_LSHIFT:"",
           p.K_RCTRL:"",
           p.K_LCTRL:"",
           p.K_RALT:"",
           p.K_LALT:"",
           p.K_RMETA:"",
           p.K_LMETA:"",
           p.K_LSUPER:"",
           p.K_RSUPER:"",
           p.K_MODE:"",
           p.K_HELP:"",
           p.K_PRINT:"",
           p.K_SYSREQ:"",
           p.K_BREAK:"",
           p.K_MENU:"",
           p.K_POWER:"",
           p.K_EURO:"€"}

def init(fontobj=None):
    global font
    if fontobj == None:
        font = pygame.font.SysFont("Arial",20,False,False)
    else:
        font = fontobj

def draw_text(txt,pos,bs,color=[0,0,0],bgcolor=[255,255,255,0],opaque=False):
    global font
    if not opaque:
        s = font.render(txt,False,color,bgcolor)
    elif opaque:
        s = font.render(txt,False,color)
    bs.blit(s,pos)

class Widget():
    def __init__(self,pos=[0,0],size=[0,0],name="widget"):
        self.pos = pos
        self.state = WIDGET_STATE_NONE
        self.size = size
        self.name = name
    def draw(self,screen):
        pass
    def onclickdown(self,e):
        self.state = WIDGET_STATE_CLICKED
    def onclickup(self,e):
        self.state = WIDGET_STATE_HOVER
    def onhover(self):
        self.state = WIDGET_STATE_HOVER
    def onunhover(self,e):
        self.state = WIDGET_STATE_NONE
    def onevent(self,e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            self.onclickdown(e)
        elif e.type == pygame.MOUSEBUTTONUP:
            self.onclickup(e)

class Button(Widget):
    def __init__(self,pos=[0,0],size=[0,0],label="",bgcolor=[242,241,240],name="button"): # bgcolor stolen from ubuntu
        Widget.__init__(self)
        self.pos = pos
        self.size = size
        self.label = label
        self.name = name
        self.handlers_click = []
        self.bgcolor = bgcolor
    def draw(self,screen):
        s = pygame.Surface(self.size)
        s.fill(self.bgcolor)
        r = pygame.Rect([0,0],self.size)
        pygame.draw.rect(s,[206,203,201],r,2) # also stolen from ubuntu
        draw_text(self.label,[((self.size[0]/2)-(font.size(self.label)[0]/2)),3],s,opaque=True)
        if self.state == WIDGET_STATE_CLICKED:
            screen.blit(s,[self.pos[0]+2,self.pos[1]+2])
        else:
            screen.blit(s,self.pos)
        return screen
    def add_handler(self,etype,func,args):
        if etype == "click":
            self.handlers_click.append([func,args])
    def onclickdown(self,e):
        Widget.onclickdown(self,e)
        for h in self.handlers_click:
            try:
                h[0](*h[1])
            except Exception:
                print("Button clickhandler raised exception")
                traceback.print_exc()

class TextBox(Widget):
    def __init__(self,pos=[0,0],size=[0,0],name="txtbox"):
        Widget.__init__(self)
        self.pos = pos
        self.size = size
        self.txt = ""
        self.name = name
        self.cpos = 0
        self.focused = False
    def get_text(self,rel="get"):
        if rel=="get":
            return self.txt
        else:
            return self.txt
        return self.txt
    def onevent(self,e):
        if e.type == pygame.KEYDOWN:
            self.append_char(e.unicode)
            print(e)
        else:
            Widget.onevent(self,e)
    def append_char(self,char):
        if char not in [u"\b",u"\r",u"\n"]:
            self.txt+=char
            self.cpos+=1
        elif char == u"\x08":
            sl = len(list(self.txt))
            s = list(self.txt)
            s = s[:-1]
            self.txt = "".join(s)
            if sl!=len(s):
                self.cpos-=1
        elif char in [u"\n",u"\r"]:
            pass # maybe add event
    def draw(self,screen):
        s = pygame.Surface(self.size)
        s.fill([245,245,245])
        r = pygame.Rect([0,0],self.size)
        pygame.draw.rect(s,[206,203,201],r,2) # color stolen from ubuntu
        draw_text(self.get_text("draw"),[2,2],s,opaque=True)
        if self.focused:
            cp1 = [font.size("".join(list(self.get_text("draw"))[:self.cpos]))[0],2]
            cp2 = [font.size("".join(list(self.get_text("draw"))[:self.cpos]))[0],self.size[1]]
            pygame.draw.line(s,[0,0,0],cp1,cp2,1)
        screen.blit(s,self.pos)
    def clear(self):
        self.txt = ""
        self.cpos = 0

class PasswordBox(TextBox):
    def __init__(self,pos=[0,0],size=[0,0],name="passwdbox"):
        TextBox.__init__(self)
        self.pos = pos
        self.size = size
        self.txt = ""
        self.vchar = "*"
        self.name = name
    def get_text(self,rel="get"):
        if rel == "get":
            return self.txt
        elif rel == "draw":
            return "".join([self.vchar for i in range(len(self.txt))])
        return self.txt

class MultiLineTextBox(TextBox):
    def __init__(self,pos=[0,0],size=[0,0],name="mltextbox"):
        TextBox.__init__(self)
        self.pos = pos
        self.size = size
        self.name = name
        self.txtlines = [""]
        self.focused = False
        self.cpos = [0,0]
    def get_text(self,rel="get"):
        return "\n".join(self.txtlines)
    def draw(self,screen):
        s = pygame.Surface(self.size)
        s.fill([245,245,245])
        r = pygame.Rect([0,0],self.size)
        pygame.draw.rect(s,[206,203,201],r,2) # color stolen from ubuntu
        for i in range(len(self.txtlines)):
            draw_text(self.txtlines[i-1],[2,23*i],s,opaque=True)
        if self.focused:
            cp1 = [font.size("".join(list(self.get_text("draw"))[:self.cpos[1]]))[0],2+(self.cpos[0]*23)]
            cp2 = [font.size("".join(list(self.get_text("draw"))[:self.cpos[1]]))[0],25+(self.cpos[0]*23)]
            pygame.draw.line(s,[0,0,0],cp1,cp2,1)
            pass
        screen.blit(s,self.pos)
        return screen
    def append_char(self,char):
        if char in [u"\r",u"\n"]:
            self.txtlines.append("")
            self.cpos[0]+=1
        elif char == u"\x08":
            s = list(self.txtlines[-1])
            s = s[:-1]
            self.txtlines[-1] = "".join(s)
            self.cpos[1]-=1
        else:
            self.cpos[1]+=1
            self.txtlines[-1]+=char
    def clear(self):
        self.txtlines = [""]

class ScrollableTextView(Widget):
    def __init__(self,pos=[0,0],size=[0,0],name="scrollTextView",editable=True):
        Widget.__init__(self)
        self.pos = pos
        self.size = size
        self.name = name
        self.editable = editable
        self.text = []
        self.scrolloffset = 0
    def draw(self,screen):
        s = pygame.Surface(self.size,pygame.SRCALPHA)
        s.fill([245,245,245])
        r = pygame.Rect([0,0],self.size)
        pygame.draw.rect(s,[206,203,201],r,2) # color stolen from ubuntu
        for line in range(len(self.text)):
            draw_text(self.text[line],[2,23*(line+self.scrolloffset)],s,opaque=True)
        screen.blit(s,self.pos)
    def add_line(self,line):
        self.text.append(line)
        self.scrolltoend()
    def scrolltoend(self):
        self.scrolloffset = (self.size[1]/23)-(len(self.text))
    def scroll(self,linenum=0):
        self.scrolloffset = linenum

class DropDownMenu(Widget):
    def __init__(self,pos=[0,0],size=[0,0],name="dropDownMenu"):
        Widget.__init__(self)
        self.pos = pos
        self.size = size
        self.name = name
        self.entrys = []
        self.extended = False
        self.focused = False
    def draw(self,screen):
        if not self.extended:
            pass
        elif self.extended:
            pass
        return screen
    def add_entry(self,entry):
        self.entrys.append(entry)
    def onevent(self,e):
        mp = pygame.mouse.

class SubWidget(Widget):
    def __init__(self,pos=[0,0],size=[0,0],name="subWidget",parent=Widget(),visible=True):
        Widget.__init__(self)
        self.pos = pos
        self.size = size
        self.name = name
        self.parent = parent
        self.visible = visible
    def draw(self):
        return pygame.Surface()

class DropDownMenuEntry(SubWidget):
    def __init__(self,pos=[0,0],size=[0,0],name="dropDownMenuEntry",parent=Widget(),visible=False,label="Entry"):
        SubWidget.__init__(self)
        self.pos = pos
        self.size = size
        self.name = name
        self.parent = parent
        self.visible = visible
        self.selected = False
        self.clickhandlers = []
        self.label = label
    def add_clickhandler(self,handler):
        self.clickhandlers.append(handler)
    def onclickdown(self,e):
        for f in self.clickhandlers:
            try:f()
            except Exception:
                pass
        self.selected = True
        Widget.onclickdown(self,e)
    def draw(self):
        s = pygame.Surface(self.size,pygame.SRCALPHA)
        s.fill([242,241,240]) # stolen from ubuntu
        draw_text()

class StaticText(Widget):
    def __init__(self,pos=[0,0],size=[0,0],name="text",label="Some Text"):
        Widget.__init__(self)
        self.pos = pos
        self.size = size
        self.name = name
        self.label = label
        self.visible = True
    def draw(self,screen):
        if self.visible:
            draw_text(self.label,self.pos,screen,opaque=True)

class MenuManager():
    def __init__(self):
        self.menus = {}
        self.menu = ""
        self.screensize = []
    def add_menu(self,menu):
        self.menus[menu.name] = menu
    def set_size(self,size):
        self.screensize = size
    def set_cur_menu(self,name):
        if name in self.menus:
            self.menu = name
        if self.menu !="":
            self.menus[self.menu].onleave()
        else:
            raise ValueError("Menu '%s' does not exist"%name)
    def get_img(self):
        s = pygame.Surface(self.screensize,pygame.SRCALPHA)
        s.fill([0,0,0,0])
        return self.menus[self.menu].draw(s)
    def get_menu(self,name):
        try:
            return self.menus[name]
        except Exception:
            raise ValueError("menu with name '%s' does not exist"%name)
    def handle_event(self,e):
        self.menus[self.menu].handle_event(e)
    def draw(self):
        return self.get_img()

class BaseMenu():
    def __init__(self):
        self.name = "BaseMenu"
        self.components = []
    def draw(self,screen):
        # probably with draw_text()
        return screen
    def handle_event(self,e):
        pass
    def onleave(self):
        pass

class Menu(BaseMenu):
    def __init__(self,name="menu"):
        BaseMenu.__init__(self)
        self.name = name
        self.compsbyname = {}
        self.focused = None
    def draw(self,screen):
        for element in self.components:
            element.draw(screen)
        return screen
    def handle_event(self,ev):
        if ev.type in [pygame.MOUSEBUTTONDOWN]:
            mposx = pygame.mouse.get_pos()[0]
            mposy = pygame.mouse.get_pos()[1]
            #handled = False
            for e in self.components:
                e.focused = False
                eposx = e.pos[0]
                eposy = e.pos[1]
                esizex = e.size[0]
                esizey = e.size[1]
                if eposx <= mposx < (eposx+esizex): # x axis check
                    if eposy <= mposy < (eposy+esizey):
                        # mabe add break here
                        #e.onevent(ev)
                        self.focused = e
                        e.focused = True
                        #handled = True
        #if handled == False:
        self.focused.onevent(ev)
    def add_component(self,comp):
        if self.components == []:
            self.focused = comp
        self.components.append(comp)
        self.compsbyname[comp.name] = comp
    def get_comp(self,name="name"):
        try:
            return self.compsbyname[name]
        except KeyError:
            raise ValueError("GUI Component '%s' does not exist"%name)
    def onleave(self):
        for e in self.components:
            e.focused = False
    
