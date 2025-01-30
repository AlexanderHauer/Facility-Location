from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bruteforce import bruteforce
from sublinear import sublinear_geometry
from randomized_bf import rand_bruteforce
import time

points = []


def bf(points, r):
    start_time = time.time()
    center = bruteforce(points, r)
    end_time = time.time()
    e = end_time - start_time
    print("Bf took " + str(e))
    if center is None:
        print("No valid center found")
        return

    center_float = (float(center[0]), float(center[1]))
    print(f"The best center is at: {center_float}")

    # Create a new window to display the result of the brute force algorithm
    bf_window = Toplevel()
    bf_window.geometry("500x500")
    bf_window.title("Brute Force Result")

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(points[:, 0], points[:, 1], color='blue', marker='o')  # Scatter the points
    ax.set_title("Brute Force Result")
    ax.grid(True)

    # Draw the circle with the found center
    circle = plt.Circle((center_float[0], center_float[1]), r, color='red', alpha=0.3, fill=True)
    ax.add_patch(circle)

    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)

    canvas = FigureCanvasTkAgg(fig, master=bf_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Display the found center coordinates
    scale_label = Label(bf_window, text=f"Best center at: {center_float[0]}, {center_float[1]}", font=("Consolas", 12))
    scale_label.pack(pady=10)


def rand_brt(points, r):
    start_time = time.time()
    center = rand_bruteforce(points, r)
    end_time = time.time()
    e = end_time - start_time
    print("Randomized Brute Force took " + str(e))
    if center is None:
        print("No valid center found")
        return

    center_float = (float(center[0]), float(center[1]))
    print(f"The best center is at: {center_float}")

    # Create a new window to display the result of the Sublinear Geometry algorithm
    crst_window = Toplevel()
    crst_window.geometry("500x500")
    crst_window.title("Randomized Brute Force result")

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(points[:, 0], points[:, 1], color='blue', marker='o')
    ax.set_title("Randomized Brute Force result")
    ax.grid(True)

    # Draw the circle with the found center
    circle = plt.Circle((center_float[0], center_float[1]), r, color='red', alpha=0.3, fill=True)
    ax.add_patch(circle)

    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)

    canvas = FigureCanvasTkAgg(fig, master=crst_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Display the found center coordinates
    scale_label = Label(crst_window, text=f"Best center at: {center_float[0]}, {center_float[1]}", font=("Consolas", 12))
    scale_label.pack(pady=10)


def s_est(points, r, sample_size):
    start_time = time.time()
    center = sublinear_geometry(points, r, sample_size)
    end_time = time.time()
    e = end_time - start_time
    print("Sampled Estimate took " + str(e))
    if center is None:
        print("No valid center found")
        return

    center_float = (float(center[0]), float(center[1]))
    print(f"The best center is at: {center_float}")

    # Create a new window to display the result of the Randomized Geometry algorithm
    ran_window = Toplevel()
    ran_window.geometry("500x500")
    ran_window.title("Sampled Estimate Result")

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(points[:, 0], points[:, 1], color='blue', marker='o')
    ax.set_title("Sampled Estimate Result")
    ax.grid(True)

    # Draw the circle with the found center
    circle = plt.Circle((center_float[0], center_float[1]), r, color='red', alpha=0.3, fill=True)
    ax.add_patch(circle)

    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)

    canvas = FigureCanvasTkAgg(fig, master=ran_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Display the found center coordinates
    scale_label = Label(ran_window, text=f"Best center at: {center_float[0]}, {center_float[1]}", font=("Consolas", 12))
    scale_label.pack(pady=10)


def exitB():
    exit(0)


def info():
    # This is just an information widget for explaining what this application does
    info_window = Toplevel()
    info_text = ("Given a number of customers n, the application randomly generates n points. Next, a radius r is "
                 "chosen.\nThe application finds the optimal location for the facility to be placed such that it "
                 "maximizes the number of customers in the area.")

    info_window.info_photo = PhotoImage(file="infolow.png")

    info_label = Label(info_window,
                       text=info_text,
                       font=('Arial', 12, 'bold'),
                       relief=RAISED,
                       bd=15,
                       padx=20,
                       pady=20,
                       image=info_window.info_photo,
                       compound='left'
                       )
    info_label.pack()


def createEmbeddedGraph(n, parent):
    global points
    points = np.column_stack((np.random.rand(n) * 1000, np.random.rand(n) * 1000))

    # Choose a fixed center for the circle
    center_x, center_y = np.mean(points, axis=0)
    initial_r = 100  # Default initial radius

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(points[:, 0], points[:, 1], color='blue', marker='o')
    ax.set_title(f"Graph with {n} Random Points")
    ax.grid(True)

    # Draw circle
    circle = plt.Circle((center_x, center_y), initial_r, color='red', alpha=0.3, fill=True)
    ax.add_patch(circle)

    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Function to update the circle dynamically
    def update_circle(val):
        r = scale.get()
        circle.set_radius(r)
        canvas.draw()

    # Scale widget
    scale = Scale(parent,
                  from_=0,
                  to=300,
                  length=420,
                  orient=HORIZONTAL,
                  font=("Consolas", 10),
                  tickinterval=50,
                  command=update_circle
                  )
    scale.set(initial_r)
    scale.place(x=50, y=400)

    rLabel = Label(parent,
                   text="r =",
                   font=('Consolas', 15, 'bold'),
                   )
    rLabel.place(x=10, y=415)

    # The different methods are available as buttons
    bruteforceB = Button(parent, text="Bruteforce", command=lambda: bf(points, scale.get()))
    bruteforceB.config(font=("Consolas", 12, "bold"))
    bruteforceB.place(x=10, y=460)

    r_bfB = Button(parent, text="Randomized Bf.", command=lambda: rand_brt(points, scale.get()))
    r_bfB.config(font=("Consolas", 12, "bold"))
    r_bfB.place(x=170, y=460)

    ss = len(points)
    ss = int(ss / 100)

    s_estB = Button(parent, text="Sampled est.", command=lambda: s_est(points, scale.get(), ss))
    s_estB.config(font=("Consolas", 12, "bold"))
    s_estB.place(x=350, y=460)


def submit():
    n = int(entry.get())
    graph_window = Toplevel()
    graph_window.geometry("500x500")
    graph_window.title("Resulting Graph")
    graph_window.iconphoto(True, icon)

    graph_window.title("Generated Graph")
    createEmbeddedGraph(n, graph_window)


window = Tk()
window.geometry("420x420")
window.title("Facility Location Finder")
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)

# The basic buttons
submit = Button(window, text="Submit", command=submit)
submit.config(font=("Consolas", 20, "bold"))
submit.place(x=280, y=350)

info = Button(window, text="Info", command=info)
info.config(font=("Consolas", 10, "bold"))
info.place(x=20, y=20)

exitB = Button(window, text="Exit", command=exitB)
exitB.config(font=("Consolas", 20, "bold"))
exitB.place(x=20, y=350)

entry = Entry()
entry.config(font=("Consolas", 20, "bold"))
entry.config(width=15)
entry.place(x=100, y=200)

entryLabel = Label(window,
                   text="Please type the number of customers",
                   font=('Consolas', 15, 'bold'),
                   relief=RAISED,
                   bd=5,
                   padx=5,
                   pady=5,
                   )
entryLabel.place(x=10, y=100)

nLabel = Label(window,
               text="n =",
               font=('Consolas', 15, 'bold'),
               )
nLabel.place(x=60, y=203)

window.mainloop()
