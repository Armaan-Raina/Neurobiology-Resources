Web Vpython 3.2
from vpython import * 

#############Scene setup#################
scene = canvas(title='Visual Pathway Simulation', width=1250, height=600, background=vector(0.95, 0.95, 0.95))
light = False
onCoffS = False
offConS = False
direct = False
indirect = False

def toggle_light(evt):
    global light
    light = evt.checked

def toggle_onCoffS(evt):
    global onCoffS
    onCoffS = evt.checked

def toggle_offConS(evt):
    global offConS
    offConS = evt.checked

def toggle_direct(evt):
    global direct
    direct = evt.checked

def toggle_indirect(evt):
    global indirect
    indirect = evt.checked

light_button = checkbox(text="Turn Light On", bind=toggle_light)
onCoffS_button = checkbox(text="On-center off-surround", bind=toggle_onCoffS)
offConS_button = checkbox(text="Off-center on-surround", bind=toggle_offConS)
direct_button = checkbox(text="Direct Pathway", bind=toggle_direct)
indirect_button = checkbox(text="Indirect Pathway", bind=toggle_indirect)
run_button = button(text="Run Simulation", bind=run_simulation)
legend = label(pos=vec(100,80,0), text="Blue: Excited Cell", color=color.blue)
legend2 = label(pos=vec(100,60,0), text="Red: Inhibited Cell", color=color.red)
#######################


########Component setup##########

##Set up rods
center_rod = cylinder(pos= vec(0,80,0), axis=vec(0,-1,0), color=color.black, radius=8, length=45)
right_rod = cylinder(pos= vec(40,80,0), axis=vec(0,-1,0), color=color.black, radius=8, length=45)
left_rod = cylinder(pos= vec(-40,80,0), axis=vec(0,-1,0), color=color.black, radius=8, length=45)

##Set up horizontal cells
left_horizontal_cell = cylinder(pos=vec(-33,32,0), axis=vec(1,0,0), color=color.black, radius=4, length=25)
right_horizontal_cell = cylinder(pos=vec(8,32,0), axis=vec(1,0,0), color=color.black, radius=4, length=25)

##Setup Bipolar cell
top_nub = sphere(pos=vec(0,23,0), color=color.black, radius=8)
bottom_nub = sphere(pos=vec(0,-28,0), color=color.black, radius=8)
middle_cell = cylinder(pos=vec(0,23,0), axis=vec(0,-1,0), color=color.black, radius=6, length=50)

##Set up RGC
nub = sphere(pos=vec(0,-50,0),color=color.black, radius=15)
stem = cylinder(pos=vec(18,-71,0),axis=vec(-1,1,0),color=color.black, radius=5,length=40)
end = cylinder(pos=vec(15,-70,0), axis=vec(1,0,0), color=color.black, radius=5, length=100)

############################

##########Function setup##########
def run_simulation():
    reset_colors_and_labels()
    if not light:
        print("Error: You must enable the light to activate the process")
        return  # Exit the function early

    if direct and indirect:
        print("Error: Both direct and indirect pathways cannot be selected simultaneously.")
        return  # Exit the function early
    
    if onCoffS and offConS:
        print("Error: Cannot have a cell with both orientations.")
        return
    
    if not direct and not indirect:
        print("Error: Must select a pathway.")
        return  # Exit the function early
    if not onCoffS and not offConS:
        print("Error: Must select a cell orientation.")
        return  # Exit the function early
    
    if direct:
        if onCoffS: #this represents the on-center off-surround direct pathway
            bipolarNT= label(pos=vec(50,23,0), text="Bipolar cells have inhibitory \n mGLUr6 receptors in this case \n (disinhibition occurs at this step)", color=color.black)
            rate(1)
            center_rod.color = color.red #light inhibits photoreceptor
            rate(1)
            top_nub.color = color.blue
            middle_cell.color = color.blue #disinhibition excites bipolar cell
            bottom_nub.color = color.blue
            rate(1)
            nub.color = color.blue
            stem.color = color.blue #bipolar cell excites RGC
            end.color = color.blue
            AP = label(pos=vec(25,-55,0), text="AP :)", color=color.black)
            rate(1)
            AP.visible = False
            bipolarNT.visible = False
            reset_colors_and_labels()
            return 
        else: #this represents the off-center on-surround direct pathway
            bipolarNT= label(pos=vec(50,23,0), text="Bipolar cells have excitatory \n AMPA receptors in this case", color=color.black)
            rate(1)
            center_rod.color = color.red #light hyperpolarizes rod
            rate(1)
            top_nub.color = color.red
            middle_cell.color = color.red #rod inhibits bipolar cell
            bottom_nub.color = color.red
            rate(1)
            nub.color = color.red
            stem.color = color.red #bipolar cell inhibits RGC
            end.color = color.red
            NoAP = label(pos=vec(25,-55,0), text="No AP :(", color=color.black)
            rate(1)
            NoAP.visible = False
            bipolarNT.visible = False
            reset_colors_and_labels()
            return
    if indirect:
        if onCoffS: #this represents the on-center off-surround indirect pathway
            bipolarNT= label(pos=vec(50,23,0), text="Bipolar cells have inhibitory \n mGLUr6 receptors in this case", color=color.black)
            rate(1)
            left_rod.color = color.red #light inhibits surround rod
            rate(1)
            left_horizontal_cell.color = color.red #less glutamate goes onto horizontal cell
            rate(1)
            center_rod.color = color.blue #disinhibition of center rod occurs
            rate(1)
            top_nub.color = color.red
            middle_cell.color = color.red #mGLUr6 inhibits bipolar cell
            bottom_nub.color = color.red
            rate(1)
            nub.color = color.red
            stem.color = color.red #bipolar cell inhibits RGC
            end.color = color.red
            NoAP = label(pos=vec(25,-55,0), text="No AP :(",color=color.black)
            rate(1)
            NoAP.visible = False
            bipolarNT.visible = False
            reset_colors_and_labels()
            return
            
        else: #this represents the off-center on-surround indirect pathway
            bipolarNT= label(pos=vec(50,23,0), text="Bipolar cells have excitatory\n AMPA receptors in this case", color=color.black)
            rate(1)
            right_rod.color = color.red #light inhibits the surround rod
            rate(1)
            right_horizontal_cell.color = color.red #less glutamate goes onto horizontal cell, inhibiting it
            rate(1)
            center_rod.color = color.blue #disinhibition of center rod occurs
            rate(1)
            top_nub.color = color.blue
            middle_cell.color = color.blue #AMPA excites bipolar cell
            bottom_nub.color = color.blue
            rate(1)
            nub.color = color.blue
            stem.color = color.blue #bipolar cell excites RGC
            end.color = color.blue
            AP = label(pos=vec(25,-55,0), text="AP :)",color=color.black)
            rate(1)
            AP.visible = False
            bipolarNT.visible = False
            reset_colors_and_labels()
            return 

def reset_colors_and_labels():
    center_rod.color = color.black
    right_rod.color = color.black
    left_rod.color = color.black
    top_nub.color=color.black
    bottom_nub.color=color.black
    middle_cell.color = color.black
    nub.color = color.black
    stem.color = color.black
    end.color = color.black
    left_horizontal_cell.color = color.black
    right_horizontal_cell.color = color.black
    


    





