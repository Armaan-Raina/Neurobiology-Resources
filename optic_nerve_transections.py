Web VPython 3.2
from vpython import *
###########Scene Setup#############

scene = canvas(title='Optic Nerve Transections', width=1250, height=600, background=vector(0.95, 0.95, 0.95))
# Zoom out and back the camera up
scene.camera.pos = vector(0, 100, 0)  # Increase the y-value for zooming out and adjust the z-value to back up
scene.camera.axis = vector(0, -1, 0) # Ensure the camera still points downward
# Set up the scene to render everything in view
scene.range = 50  # Increase this to ensure the entire scene is visible
scene.fov = 0.01  # Narrower field of view to avoid the need to zoom manually



# Initialize variables
preChiasmR = False
preChiasmL = False
chiasmVert = False
chiasmHoriz = False
postChiasmR = False
postChiasmL = False

def set_transection(evt):
    global preChiasmR, preChiasmL, chiasmVert, chiasmHoriz, postChiasmR, postChiasmL
    selected = evt.selected
    
    # Ignore the initial "Select transection" option
    if selected == "Select transection":
        return

    # Reset all variables to False first
    preChiasmR = preChiasmL = chiasmVert = chiasmHoriz = postChiasmR = postChiasmL = False
    
    if selected == "Before the chiasm on the right":
        preChiasmR = True
    elif selected == "Before the chiasm on the left":
        preChiasmL = True
    elif selected == "Vertically on the chiasm":
        chiasmVert = True
    elif selected == "Horizontally on the chiasm":
        chiasmHoriz = True
    elif selected == "After the chiasm on the right":
        postChiasmR = True
    elif selected == "After the chiasm on the left":
        postChiasmL = True

# Create a menu to choose transection points
menu(text="Choose Transection Point", choices=["Select transection", 
                                               "Before the chiasm on the right", 
                                               "Before the chiasm on the left", 
                                               "Vertically on the chiasm", 
                                               "Horizontally on the chiasm", 
                                               "After the chiasm on the right", 
                                               "After the chiasm on the left"], 
     bind=set_transection)

run = button(text="Run Simulation", bind=run_simulation)
legend = label(pos=vec(55,55,20), text="Black: Nerve death", color=color.black)

###################################

##########Component setup##########

left_eye = sphere(pos=vec(20,0,-10), radius=6, color=color.white)
left_pupil = sphere(pos=vec(20,0,-5), radius=2.5, color=color.black)
right_eye = sphere(pos=vec(-20,0,-10), radius=6, color=color.white)
right_pupil = sphere(pos=vec(-20,0,-5), radius=2.5, color=color.black)
LPC = cylinder(pos=vec(20,0,-10), radius=2, color=color.blue, length=25, axis=vec(-1,0,-1))
RPC = cylinder(pos=vec(-20,0,-10), radius=2,color=color.red, length=25, axis=vec(1,0,-1))
LL = cylinder(pos=vec(5,0,-25), radius=1, color=color.red, length=10, axis=vec(0,0,-1))
LR = cylinder(pos=vec(7,0,-22), radius=1, color=color.blue, length=20, axis=vec(-1,0,-1))
RR = cylinder(pos=vec(-5,0,-25),radius=1, color=color.blue, length=10, axis=vec(0,0,-1))
RL = cylinder(pos=vec(-7,0,-22),radius=1, color=color.red, length=20, axis=vec(1,0,-1))
LPC1 = cylinder(pos=vec(-5,0,-34), radius=2, color=color.blue, length=25, axis=vec(-1,0,-1))
RPC1 = cylinder(pos=vec(5,0,-34), radius=2,color=color.red, length=25, axis=vec(1,0,-1))

LMa = arrow(pos=vec(11.5, 0, -10), axis=vec(20, 0, 20), shaftwidth=0.5, color=color.blue)
LLa = arrow(pos=vec(28.5, 0, -10), axis=vec(-20, 0, 20), shaftwidth=0.5, color=color.red)
RLa = arrow(pos=vec(-28.5, 0, -10), axis=vec(20, 0, 20), shaftwidth=0.5, color=color.blue)
RMa = arrow(pos=vec(-11.5, 0, -10), axis=vec(-20, 0, 20), shaftwidth=0.5, color=color.red)

#######################################

def run_simulation():
    
    if preChiasmR:
        result = label(pos=vec(0,20,20), text="Right peripherial vision is lost", color=color.black)
        rate(1)
        RPC.color=color.black
        RR.color=color.black
        RL.color=color.black
        rate(1)
        RMa.visible = False
        rate(1)
        rate(1)
        result.visible=False
        reset_colors_and_arrows()
        return
        
    elif preChiasmL:
        result = label(pos=vec(0,20,20), text="Left peripheral vision is lost", color=color.black)
        rate(1)
        LPC.color = color.black
        LL.color = color.black
        LR.color = color.black
        rate(1)
        LMa.visible = False
        rate(1)
        rate(1)
        result.visible=False
        reset_colors_and_arrows()
        return
    
    elif chiasmVert:
        result = label(pos=vec(0,20,20), text="All peripheral vision is lost", color=color.black)
        rate(1)
        LR.color = color.black
        RL.color = color.black
        rate(1)
        LMa.visible = False
        RMa.visible = False
        rate(1)
        rate(1)
        result.visible = False
        reset_colors_and_arrows()
        return
        
    elif chiasmHoriz:
        RPC.color = color.black
        LPC.color = color.black
        rate(1)
        RR.color = color.black
        RL.color = color.black
        LL.color = color.black
        LR.color = color.black
        rate(1)
        RPC1.color = color.black
        LPC1.color = color.black
        rate(1)
        LLa.visible = False
        LMa.visible = False
        RLa.visible = False
        RMa.visible = False
        rate(1)
        result = label(pos=vec(0,20,20), text="Ur cooked💀", color=color.black)
        rate(1)
        rate(1)
        result.visible = False
        reset_colors_and_arrows()
        return
        
    elif postChiasmL:
        result = label(pos=vec(0,20,20), text="Right field of vision (medial and peripheral) is lost", color=color.black)
        rate(1)
        RPC1.color = color.black
        rate(1)
        RMa.visible = False
        RLa.visible = False
        rate(1)
        result.visible = False
        reset_colors_and_arrows()
        return
        
    elif postChiasmR:
        result = label(pos=vec(0,20,20), text="Left field of vision (medial and peripheral) is lost", color=color.black)
        rate(1)
        LPC1.color = color.black
        rate(1)
        LMa.visible = False
        LLa.visible = False
        rate(1)
        rate(1)
        result.visible = False
        reset_colors_and_arrows()
        return
    
    else:
        print("Please select an option")


    

def reset_colors_and_arrows():
    # Reset the colors of the cylinders (optic nerve segments)
    RPC.color = color.red
    LPC.color = color.blue
    RR.color = color.blue
    RL.color = color.red
    LL.color = color.red
    LR.color = color.blue
    RPC1.color = color.red
    LPC1.color = color.blue

    # Make the arrows visible again
    RLa.visible=True
    RMa.visible=True
    LLa.visible=True
    LMa.visible=True
