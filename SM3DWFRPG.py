import pygame
from math import sqrt, sin, cos, tan
from random import random


# a class which manages vectors such as points in 3D space
class Vertex:
    def __init__(self, x = 0, y = 0, z = 0, c = (255,255,255)):
        self.x = x
        self.y = y
        self.z = z
        self.c = c # color, only used sometimes
        
    def add(self,v):
        sum = self.copy()
        sum.x += v.x
        sum.y += v.y
        sum.z += v.z
        return sum
    
    def become(self,v):
        self.x = v.x
        self.y = v.y
        self.z = v.z
        
    def distance_to(self, v):
        return sqrt((v.x -self.x)**2 + (v.y -self.y)**2 + (v.z -self.z)**2)
        
    
    def copy(self): return Vertex(self.x, self.y, self.z, self.c)





class SM3DWFRPG: # Super Minimal 3D Wireframe Renderer in Pygame
    
    def __init__(self, screen_res = (500, 500), bg_color = (255,255,255), fov = 70, offset = Vertex(0,0,0)):
    
        self.SCREEN_RES = screen_res
        self.BG_COLOR = bg_color
        self.FOV = (fov/180)*3.14 # converting deg to rad
        self.offset = offset
        
        # pygame stuff
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREEN_RES)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('SM3DWFRPG')
        
        self.renderQueue = [] # an array which stores either 3D points or lines, which should be rendered in the current frame
        
        # precalulations for the projection of 3D points or lines to the 2D screen
        self._Yinv_tan_f2 = 1/(tan(self.FOV/2))
        self._Xtimes_aspect = self._Yinv_tan_f2 * self.SCREEN_RES[1] / self.SCREEN_RES[0]
     
    def draw(self):
        # pygame stuff
        pygame.display.update()
        pygame.event.pump()
        
        self.clock.tick(60)
        
        self.screen.fill(self.BG_COLOR)
        
        for call in self.renderQueue:
            if isinstance(call,Vertex): # 3D point stored in renderQueue as Vertex object
                
                x, y = self.convertTo2D(call.add(self.offset))
                self.screen.set_at((x,y), call.c)
                
            if isinstance(call, tuple): # 3D line stored as a tuple of two Vertex objects
                p0 = (self.convertTo2D(call[0].add(self.offset)))
                p1 = (self.convertTo2D(call[1].add(self.offset)))
                
                pygame.draw.line(self.screen, call[0].c, p0, p1)
    
        self.renderQueue.clear()
        
    
    def convertTo2D(self, v): # multiplying a 3-dimensional vector by the projection matrix
        
        x = (v.x*self._Xtimes_aspect)/v.z
        y = (v.y*self._Yinv_tan_f2)/v.z
                
        x = (x+1)/2 * self.SCREEN_RES[0] # the projection matrix gives point between -1 and 1
        y = (y+1)/2 * self.SCREEN_RES[1]
        
        return int(x), int(y) # screen space coordinates should always be int

    # functions to add certain objects to the renderQueue
    def point(self,point):
        self.renderQueue.append(point)

    def cube(self, point, a, rot_y = 0, color = (255,255,255)): # a - side length
        A = Vertex(0,0,0,color)
        
        B = Vertex(0,0,a,color)
                    
        C = Vertex(a,0,a,color)
                    
        D = Vertex(a,0,0,color)
        
        E = Vertex(0,a,0,color)
        
        F = Vertex(0,a,a,color)
                    
        G = Vertex(a,a,a,color)
                    
        H = Vertex(a,a,0,color)

        for p in (A,B,C,D,E,F,G,H): # rotating all points by the angle rot_y (vector multiplied by y-rotation matrix)
            v = Vertex()
            
            p.become(p.add(Vertex(-a/2,-a/2,-a/2)))
            
            v.x = p.x*cos(rot_y) - p.z*sin(rot_y)
            v.y = p.y
            v.z = p.x*sin(rot_y) + p.z*cos(rot_y)
            
            v = v.add(point)
            
            p.become(v)
            
        lines = []
        lines.append((A,B))
        lines.append((B,C))
        lines.append((C,D))
        lines.append((D,A))
        
        lines.append((E,F))
        lines.append((F,G))
        lines.append((G,H))
        lines.append((H,E))
        
        lines.append((A,E))
        lines.append((B,F))
        lines.append((C,G))
        lines.append((D,H))
        
        self.renderQueue.extend(lines)
        
        
    def sphere(self, point, r, color=(255,255,255), rot_y = 0, alp_inc = 6.28/20, bet_inc = 6.28/10):
        points = []
        
        # "standing" circles
        beta = 0
        while beta<=6.28:
            alph = 0
            while alph<=6.28:
                v0 = Vertex( cos(alph)*r*cos(beta),
                            sin(alph)*r,
                            cos(alph)*r*sin(beta),
                            color
                            )
                v1 = Vertex( cos(alph+alp_inc)*r*cos(beta),
                            sin(alph+alp_inc)*r,
                            cos(alph+alp_inc)*r*sin(beta),
                            color
                            )
                points.append((v0,v1))
                
                alph += alp_inc*2
            
            beta += bet_inc
        
        for p0,p1 in points:
            
            for p in (p0,p1): # same as above for the cube
                v = Vertex()
                
                v.x = p.x*cos(rot_y) - p.z*sin(rot_y)
                v.y = p.y
                v.z = p.x*sin(rot_y) + p.z*cos(rot_y)
                
                v = v.add(point)
                
                p.become(v)
        
        self.renderQueue.extend(points)
