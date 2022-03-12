from SM3DWFRPG import *


def main():
    renderer = SM3DWFRPG(screen_res = (700,700), bg_color = (100,100,100), offset = Vertex(0,0,1), fov = 70)
    
    # handling pygame font and text
    pygame.font.init()
    font_title = pygame.font.Font("Pixellari.ttf",27)
    font_text = pygame.font.Font("Pixellari.ttf",20)
    
    title_text = font_title.render('3-dimensional "Monte Carlo" method to approximate Pi', False, (0,0,0))
    approx_text = font_text.render(f"points in sphere / all points * 6 =", False, (0,0,0))
    best_approx_text = font_title.render("0", False, (100,0,0))
    
    r = 0 # rotation variable
     
    best_approx = 0
    pi = 3.141592653589793238 # to display the best approximation
    
    # object specifications
    cube_a = 2
    sphere_r = cube_a/2
    
    obj_pos = Vertex(0,0,3)
    
    p_sphere = 0 # points in the sphere
    p_cube = 0 # all points
    all_points = []
    
    while True:
        
        rng_v = Vertex( random()*cube_a -cube_a/2,
                        random()*cube_a -cube_a/2,
                        random()*cube_a -cube_a/2,
                        (0,255,255)
                        )
        p_cube += 1 # the point will always be in the cube
        
        # changing color and incrementing the sphere count if the point is in the sphere
        dst = rng_v.distance_to(Vertex(0,0,0)) 
        if dst<=sphere_r:
            p_sphere += 1
            rng_v.c = (0,255,0)
        
        # to avoid a massive slowdown, just stop drawing additional points from this point on
        if len(all_points)<= 4000: 
            all_points.append(rng_v)
        
        for p in all_points: # rotate all points
            v = Vertex()
                
            v.x = p.x*cos(r) - p.z*sin(r)
            v.y = p.y
            v.z = p.x*sin(r) + p.z*cos(r)
            v.c = p.c
            renderer.point(v.add(obj_pos))
            
            
        current_approx = (p_sphere/p_cube)*6
        

        if abs(best_approx-pi) > abs(current_approx-pi):
            best_approx = current_approx
            best_approx_text = font_title.render(f"{best_approx}", False, (100,0,0))
            
            
        approx_text = font_text.render(f"points in sphere / all points * 6 = {current_approx}", False, (0,0,0))

        renderer.screen.blit(title_text, (350-title_text.get_width()//2,75-title_text.get_height()//2))
        renderer.screen.blit(approx_text, (100,600))
        renderer.screen.blit(best_approx_text, (350-best_approx_text.get_width()//2,650))
        
        
        renderer.cube(obj_pos, cube_a, rot_y=r, color=(150,150,150))
        renderer.sphere(obj_pos, sphere_r, rot_y=r, color=(150,100,100))
        
        renderer.draw()
        
        # so that it is rotating at a constant speed even if the frames per second are different take fps into account
        fps = renderer.clock.get_fps()
        if fps != 0: r += 0.005 * 60/fps
        
        
if __name__ == "__main__":
    main()