import tkinter
import tkinter.messagebox
import customtkinter
import subprocess

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Colour Recognition Application.py")
        #self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        #creating a label
        self.label = customtkinter.CTkLabel(self, text_color="#1C86EE", text = "Colour Recognition Application", font=("Alexandria", 50))
        self.label.grid(row=0, column=1, padx=(0, 0), pady=(0, 0))

        #creating a textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250, font=("Alexandria", 15))
        self.textbox.grid(row=1, column=1, padx=(300, 300), pady=(0, 5), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=2, column=1, padx=(300, 300), pady=(5, 5), sticky="nsew")
        self.tabview.add("Single Pixel Colour Recognition")
        self.tabview.add("Colour Tracking")
        self.tabview.add("Dominant Colour Recognition")
        self.tabview.tab("Single Pixel Colour Recognition").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Colour Tracking").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Dominant Colour Recognition").grid_columnconfigure(0, weight=1)

        #defining a seperate colour picker window
        def create_cp_window():

            cp_window = customtkinter.CTkToplevel()
            cp_window.title("Colour picker window")
            cp_window.wm_attributes("-topmost", True)

            cp_window.white_button = customtkinter.CTkButton(cp_window, text="WHITE", fg_color= "white", text_color= "black")
            cp_window.white_button.grid(row=0, column=1, padx=20, pady=(10, 0))
            cp_window.gray_button = customtkinter.CTkButton(cp_window, text="GRAY", fg_color= "gray", text_color= "black")
            cp_window.gray_button.grid(row=1, column=1, padx=20, pady=(10, 0))
            cp_window.black_button = customtkinter.CTkButton(cp_window, text="BLACK", fg_color= "black", text_color= "white")
            cp_window.black_button.grid(row=2, column=1, padx=20, pady=(10, 0))
            cp_window.red_button = customtkinter.CTkButton(cp_window, text="RED", fg_color= "red", text_color= "black")
            cp_window.red_button.grid(row=3, column=1, padx=20, pady=(10, 0))
            cp_window.brown_button = customtkinter.CTkButton(cp_window, text="BROWN", fg_color= "brown", text_color= "black")
            cp_window.brown_button.grid(row=4, column=1, padx=20, pady=(10, 0))
            cp_window.orange_button = customtkinter.CTkButton(cp_window, text="ORANGE", fg_color= "orange", text_color= "black")
            cp_window.orange_button.grid(row=5, column=1, padx=20, pady=(10, 0))
            cp_window.yellow_button = customtkinter.CTkButton(cp_window, text="YELLOW", fg_color= "yellow", text_color= "black", command= self.run_yellow_ct_mode)
            cp_window.yellow_button.grid(row=6, column=1, padx=20, pady=(10, 0))
            cp_window.green_button = customtkinter.CTkButton(cp_window, text="GREEN", fg_color= "green", text_color= "black", command= self.run_green_ct_mode)
            cp_window.green_button.grid(row=7, column=1, padx=20, pady=(10, 0))
            cp_window.cyan_button = customtkinter.CTkButton(cp_window, text="CYAN", fg_color= "cyan", text_color= "black", command= self.run_cyan_ct_mode)
            cp_window.cyan_button.grid(row=8, column=1, padx=20, pady=(10, 0))
            cp_window.blue_button = customtkinter.CTkButton(cp_window, text="BLUE", fg_color= "blue", text_color= "black", command= self.run_blue_ct_mode)
            cp_window.blue_button.grid(row=9, column=1, padx=20, pady=(10, 0))
            cp_window.purple_button = customtkinter.CTkButton(cp_window, text="PURPLE", fg_color= "purple", text_color= "black", command= self.run_purple_ct_mode)
            cp_window.purple_button.grid(row=10, column=1, padx=20, pady=(10, 0))
            cp_window.pink_button = customtkinter.CTkButton(cp_window, text="PINK", fg_color= "pink", text_color= "black", command= self.run_pink_ct_mode)
            cp_window.pink_button.grid(row=11, column=1, padx=20, pady=(10, 0))
        

        self.spcr_run_button = customtkinter.CTkButton(self.tabview.tab("Single Pixel Colour Recognition"), 
                                                       text="Run Single Pixel Colour Recognition Mode",
                                                        command=self.run_spcr_mode)
        self.spcr_run_button.grid(row=2, column=0, padx=20, pady=(10, 0))

        self.spcr_run_button = customtkinter.CTkButton(self.tabview.tab("Colour Tracking"), 
                                                       text="Run Colour Tracking Mode", 
                                                       command = create_cp_window)
        self.spcr_run_button.grid(row=2, column=0, padx=20, pady=(10, 0))

        self.spcr_run_button = customtkinter.CTkButton(self.tabview.tab("Dominant Colour Recognition"), 
                                                       text="Run Dominant Colour Recognition Mode",
                                                        command=self.run_dcr_mode)
        self.spcr_run_button.grid(row=2, column=0, padx=20, pady=(10, 0))

        #the below modules are yet to be coded
        """
        self.spcr_run_button = customtkinter.CTkButton(self.tabview.tab("Colour Tracking"), text="Run Colour Tracking Mode",
                                                           command=self.run_ct_mode)
        self.spcr_run_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.spcr_run_button = customtkinter.CTkButton(self.tabview.tab("Dominant Colour Recognition"), text="Run Dominant Colour Recognition Mode",
                                                           command=self.run_dcr_mode)
        self.spcr_run_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        """
        #creating textboxes within each tab
        self.textbox1 = customtkinter.CTkTextbox(self.tabview.tab("Single Pixel Colour Recognition"), width=250, font=("Alexandria", 15))
        self.textbox1.grid(row=0, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.textbox2 = customtkinter.CTkTextbox(self.tabview.tab("Colour Tracking"), width=250, font=("Alexandria", 15))
        self.textbox2.grid(row=0, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.textbox3 = customtkinter.CTkTextbox(self.tabview.tab("Dominant Colour Recognition"), width=250, font=("Alexandria", 15))
        self.textbox3.grid(row=0, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")

        # set default values

        self.textbox.insert("0.0", "Welcome to the Colour Recognition Application! The primary function of this application will allow you to recognize and identify the many different colours in your surrounding!\n" 
                            + "This application consists of 3 modes, displayed below, that will aid you in colour recognition. Make sure to read the instructions on how to operate each mode. Feel free to try them all!")
        self.textbox.configure(state='disabled')
        self.textbox1.insert("0.0", "The Single Pixel Colour Recognition mode will detect the colour of the object placed in the middle of the screen and display the name of the colour, in real time.\n\n" + "This mode will have cross hairs in the middle of the screen which will highlight a single pixel. Place the colour of the object you wish to scan in the middle of these crosshairs. The color of the object will be recognized, and the name of the color will be displayed at the top left corner, in real time.")
        self.textbox1.configure(state='disabled')
        self.textbox2.insert("0.0", "The Colour Tracking mode will highlight a specific chosen colour in your environment, in real time.\n\n" + "Select a colour you wish to be tracked from the given colour palette and the application will highlight all instances of that single, specific colour that is present in the field of view of the camera, in real time. It will do so by visually enclosing that colour with a visible rectangular box on the screen, constantly tracking the position of it.")
        self.textbox2.configure(state='disabled')
        self.textbox3.insert("0.0", "The Dominant Colour Recognition mode will tell you what the most abundant colour in your environment is, in real time.\n\n" + "This mode detects the most dominant colour in the field of view of the camera and displays the name of the colour at the top left corner, in real time.")
        self.textbox3.configure(state='disabled')
    
    def run_spcr_mode(self):
        subprocess.run(["python", "spcr_module.py"])

    def run_dcr_mode(self):
        subprocess.run(["python", "dcr_module.py"])    

    def run_yellow_ct_mode(self):
        subprocess.run(["python", "yellow_ct_module.py"])

    def run_green_ct_mode(self):
        subprocess.run(["python", "green_ct_module.py"]) 

    def run_cyan_ct_mode(self):
        subprocess.run(["python", "cyan_ct_module.py"]) 

    def run_blue_ct_mode(self):
        subprocess.run(["python", "blue_ct_module.py"])   

    def run_purple_ct_mode(self):
        subprocess.run(["python", "purple_ct_module.py"]) 

    def run_pink_ct_mode(self):
        subprocess.run(["python", "pink_ct_module.py"])              


    #the below modules are yet to be coded
    """
    def run_ct_mode(self):
        subprocess.run(["python", ""])

    def run_dcr_mode(self):
        subprocess.run(["python", ""])
        """   

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
