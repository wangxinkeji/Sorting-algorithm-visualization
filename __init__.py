#coding=gbk
import copy
import random
import os
import sys
import re
from matplotlib import pyplot as plt
from matplotlib import animation
titles = [ r'Bubble Sort ($O(n^2)$)', r'Selection Sort ($O(n^2)$)',
          r'Insertion Sort ($O(n^2)$)', ]

class Data:
    # Total of data to sort
    data_count = 20

    def __init__(self, value):
        self.value = value
        self.set_color()

    def set_color(self, rgba = None):
        if not rgba:
            rgba = (0,
                    1 - self.value / (self.data_count * 2),
                    self.value / (self.data_count * 2) + 0.5,
                    1)
        self.color = rgba
def create_original_data(): 
        data = list(range(1, Data.data_count + 1))
        random.shuffle(data) 
        return data
#冒泡排序
def bubble_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    for i in range(Data.data_count-1):
        flag = False
        for j in range(Data.data_count-i-1):
            if ds[j].value > ds[j+1].value:
                ds[j], ds[j+1] =  ds[j+1], ds[j]
                flag = True
            # FRAME OPERATION BEGIN
            frames.append(copy.deepcopy(ds))
            frames[-1][j+1].set_color('r')
            # FRAME OPERATION END
        if not flag:
            break
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames
#选择排序
def selection_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    for i in range(0, Data.data_count-1):
        for j in range(i+1, Data.data_count):
            # FRAME OPERATION BEGIN
            ds_r = copy.deepcopy(ds)
            frames.append(ds_r)
            ds_r[i].set_color('r')
            ds_r[j].set_color('k')
            # FRAME OPERATION END
            if ds[j].value < ds[i].value:
                ds[i], ds[j] = ds[j], ds[i]
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames

#插入排序
def insertion_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    for i in range(1, Data.data_count):
        # FRAME OPERATION BEGIN
        frames.append(copy.deepcopy(ds))
        frames[-1][i].set_color('r')
        # FRAME OPERATION END
        for j in range(i, 0, -1):
            if ds[j].value < ds[j-1].value:
                ds[j], ds[j-1] = ds[j-1], ds[j]
                # FRAME OPERATION BEGIN
                frames.append(copy.deepcopy(ds))
                frames[-1][j-1].set_color('r')
                # FRAME OPERATION END
            else:
                break
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames   
 
funs = [bubble_sort, selection_sort,insertion_sort,]
def draw_all_charts(original_data, frame_interval):
    # First set up the figure, the axis, and the plot elements we want to animate.
    axs = []
    frames = []
    fig = plt.figure(1, figsize=(10, 5))
    data_set = [Data(d) for d in original_data]
    for i in range(3):
        axs.append(fig.add_subplot(311 + i))
        axs[-1].set_xticks([])
        axs[-1].set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)

    # Get the data of all frames.
    for i in range(3):
        frames.append(funs[i](data_set))
    # The frame count of monkey sort is 50 more than the maximum one.
    #frames.append(funs[3](data_set, max(len(f) for f in frames) + 50))

    # Output the frame counts of all chart.
    names = []
    max_name_length = 0
    frame_counts = []
    max_frame_length = 0
    for i in range(3):
        names.append(re.findall(r'\w+ Sort', titles[i])[0] + ':')
        if len(names[-1]) > max_name_length:
            max_name_length = len(names[-1])
        frame_counts.append(len(frames[i]))
        if len(str(frame_counts[-1])) > max_frame_length:
            max_frame_length = len(str(frame_counts[-1]))
    for i in range(3):
        print('%-*s %*d frames' % (max_name_length, names[i], max_frame_length, frame_counts[i]))

    # Animation function. This is called sequentially.
    # Note: fi is framenumber.
    def animate(fi):
        bars = []
        for i in range(3):
            if(len(frames[i]) > fi):
                axs[i].cla()
                axs[i].set_title(titles[i])
                axs[i].set_xticks([])
                axs[i].set_yticks([])
                bars += axs[i].bar(list(range(Data.data_count)),           # X
                                   [d.value for d in frames[i][fi]],       # data
                                   1,                                      # width
                                   color=[d.color for d in frames[i][fi]]  # color
                                   ).get_children()
        return bars

    # Call the animator.
    anim = animation.FuncAnimation(fig, animate, frames=max(len(f) for f in frames), interval=frame_interval)
    return plt, anim
od = create_original_data()
plt, _ = draw_all_charts(od,700) 
plt.show()
