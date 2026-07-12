#importing libraries
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider
import numpy as np

#Menu box
def main_menu():
    while True:
        print("Double Slit Interference Simulator")
        print("1. Manual Mode")
        print("2. Slider mode")
        print("3. Exit")
        
        #input mode
        try:
            choice=int(input("Choose a mode:"))
        except ValueError:
            print("Invalid input.Enter a number from 1 to 2.")
            continue
        if choice==1:
            manual_mode()
        elif choice==2:
            slider_mode()
        elif choice==3:
            print("Exiting the simulator.Goodbye")
            break
        else:
            print("Choose a valid option(1-2).")
            
#Computes the normalized double-slit interference pattern including the single-slit diffraction envelope.
def calculate_intensity(screen_distance,wavelength,distance_btw_slits,slit_width,X_vals):
    return(((np.sin((np.pi*slit_width*X_vals)/(wavelength*screen_distance)))/((np.pi*slit_width*X_vals)/(wavelength*screen_distance)))**2)*((np.cos((np.pi*distance_btw_slits*X_vals)/(wavelength*screen_distance)))**2)

#X-axis range 
X_vals=np.arange(-0.005,0.005,0.00001)

#unit conversion
cm=10**-2
nm=10**-9
mm=10**-3
micrometer=10**-6

#manual mode                                                                                                                                        
def manual_mode():
    #user input
    screen_distance=float(input("Enter screen distance(cm):"))
    wavelength=float(input("Enter wavelength(nm):"))
    distance_btw_slits=float(input("Enter distance between slits(mm):"))
    slit_width=float(input("Enter slit width(micrometer):"))

    screen_distance=screen_distance*cm
    wavelength=wavelength*nm
    distance_btw_slits=distance_btw_slits*mm
    slit_width=slit_width*micrometer

    #Compute and plot the interference pattern
    Y_vals=calculate_intensity(screen_distance,wavelength,distance_btw_slits,slit_width,X_vals)
    plot,=plt.plot(X_vals*1000,Y_vals,color='red')
    plt.xlabel("Distance from center, x (mm)")
    plt.ylabel("Normalized Intensity (a.u.)")
    plt.title("Double Slit Interference Simulator")
    plt.show()

#slider mode
def slider_mode():
    #default values
    screen_distance=50*cm
    wavelength=500*nm
    distance_btw_slits=1*mm
    slit_width=100*micrometer

    #Compute and plot the interference pattern
    fig,ax=plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    Y_vals=calculate_intensity(screen_distance,wavelength,distance_btw_slits,slit_width,X_vals)
    plot,=ax.plot(X_vals*1000,Y_vals,color='red')
    ax.set_xlabel("Distance from center, x (mm)")
    ax.set_ylabel("Normalized Intensity (a.u.)")
    ax.set_title("Double Slit Interference Simulator")

    #axes points for sliders
    screen_distance_ax=plt.axes([0.7,0.04,0.2,0.07])
    wavelength_ax=plt.axes([0.15,0,0.2,0.07])
    distance_btw_slits_ax=plt.axes([0.15,0.04,0.2,0.07])
    slit_width_ax=plt.axes([0.7,0,0.2,0.07])

    screen_distance_slider=Slider(screen_distance_ax,"Screen Distance(cm)",10,100,valinit=screen_distance*10**2)
    wavelength_slider=Slider(wavelength_ax,"Wavelength(nm)",100,1000,valinit=wavelength*10**9)
    distance_btw_slits_slider=Slider(distance_btw_slits_ax,"Distance b/w slits(mm)",0.1,10,valinit=distance_btw_slits*10**3)
    slit_width_slider=Slider(slit_width_ax,"Slit Width(µm)",10,1000,valinit=slit_width*10**6)

    #Live update on interference pattern as slider values change 
    def update(val):
        screen_distance=screen_distance_slider.val*cm
        wavelength=wavelength_slider.val*nm
        distance_btw_slits=distance_btw_slits_slider.val*mm
        slit_width=slit_width_slider.val*micrometer
        Y_vals=calculate_intensity(screen_distance,wavelength,distance_btw_slits,slit_width,X_vals) 
        plot.set_ydata(Y_vals)
        fig.canvas.draw_idle()

    screen_distance_slider.on_changed(update)
    wavelength_slider.on_changed(update)
    distance_btw_slits_slider.on_changed(update)
    slit_width_slider.on_changed(update)
    plt.show()

#Recalling my menu box 
if __name__ == "__main__":
    main_menu()
