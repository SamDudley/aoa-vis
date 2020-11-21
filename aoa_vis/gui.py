import math
import tkinter as tk

import numpy as np
from sklearn.cluster import DBSCAN


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.angles = tk.StringVar(value="90, 91, 140, 94")
        self.eps = tk.IntVar(value=3)
        self.min_samples = tk.IntVar(value=2)

        self.angle_ids = []

        self.create_widgets()
        self.update_canvas()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        # centre point
        self.canvas.create_oval(196, 196, 204, 204, fill="#fff")
        # outer circle
        self.canvas.create_oval(8, 8, 392, 392, outline="#fff")

        self.angles_entry = tk.Entry(self.master, textvariable=self.angles)
        self.angles_entry.pack()

        self.eps_entry = tk.Entry(self.master, textvariable=self.eps)
        self.eps_entry.pack()

        self.min_samples_entry = tk.Entry(self.master, textvariable=self.min_samples)
        self.min_samples_entry.pack()

        self.render_button = tk.Button(
            self.master, text="Render", command=self.update_canvas
        )
        self.render_button.pack()

    def update_canvas(self):
        for angle_id in self.angle_ids:
            self.canvas.delete(angle_id)

        self.angle_ids = []

        angles = np.array([])

        if self.angles.get():
            angles = np.array(list(map(float, self.angles.get().split(", "))))

        self.draw_angles(angles)
        self.draw_clusters(angles)

    def draw_angles(self, angles, colour="green"):
        centre = (200, 200)
        r = 196

        for angle in angles:
            x = centre[0] + r * math.sin(math.radians(angle))
            y = centre[1] + r * math.cos(math.radians(angle))

            angle_id = self.canvas.create_line(
                centre[0], centre[1], x, 400 - y, fill=colour
            )

            self.angle_ids.append(angle_id)

    def draw_clusters(self, angles):
        if not angles.size:
            return

        clustering = DBSCAN(eps=self.eps.get(), min_samples=self.min_samples.get()).fit(
            angles.reshape(-1, 1)
        )

        labels = clustering.labels_
        unique_labels = set(labels)
        core_sample_mask = np.zeros_like(labels, dtype=bool)
        core_sample_mask[clustering.core_sample_indices_] = True

        print(labels)
        print(unique_labels)

        cluster_angles = []

        for l in unique_labels:
            # don't show noise
            if l == -1:
                continue

            cluster_member_mask = labels == l

            cluster = angles[core_sample_mask & cluster_member_mask]
            cluster_angles.append(np.average(cluster))

        self.draw_angles(cluster_angles, colour="blue")


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
