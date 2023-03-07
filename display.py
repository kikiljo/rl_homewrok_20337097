import log_reader as lr
import numpy as np
import matplotlib.pyplot as plt

# simple episodic MDP
spmdp_name1 = "./logs/Maxmin_simple/1/log.txt"
spmdp_name2 = "./logs/Maxmin_simple/2/log.txt"
spmdp_name3 = "./logs/Maxmin_simple/3/log.txt"
spmdp_name4 = "./logs/Maxmin_simple/4/log.txt"
spmdp_name5 = "./logs/Maxmin_simple/5/log.txt"
spmdp_name6 = "./logs/Maxmin_simple/6/log.txt"

spmdp_y1 = lr.openfile(spmdp_name1)
spmdp_y2 = lr.openfile(spmdp_name2)
spmdp_y3 = lr.openfile(spmdp_name3)
spmdp_y4 = lr.openfile(spmdp_name4)
spmdp_y5 = lr.openfile(spmdp_name5)
spmdp_y6 = lr.openfile(spmdp_name6)

x = np.array(range(40))
x6 = np.array(range(len(spmdp_y6)))

plt.figure(figsize=(20, 10), dpi=100)
plt.xlabel("episodes")
plt.ylabel("expected values")
plt.plot(x * 100, spmdp_y1[:40], label = "Q-Learning", color = "r")
plt.plot(x * 100, spmdp_y2[:40], label = "DDQN", color = "b")
plt.plot(x * 100, spmdp_y3[:40], label = "Maxmin N = 2", color = "green")
plt.plot(x * 100, spmdp_y4[:40], label = "Averaged N = 2", color = "y")
plt.plot(x * 100, spmdp_y5[:40], label = "Maxmin N = 4", color = "pink")
plt.plot(x6 * 100, spmdp_y6, label = "Averaged N = 4", color = "orange")

plt.legend()
plt.show()


spmdp_name1 = "./logs/Maxmin_simple2/1/log.txt"
spmdp_name2 = "./logs/Maxmin_simple2/2/log.txt"
spmdp_name3 = "./logs/Maxmin_simple2/3/log.txt"
spmdp_name4 = "./logs/Maxmin_simple2/4/log.txt"
spmdp_name5 = "./logs/Maxmin_simple2/5/log.txt"
spmdp_name6 = "./logs/Maxmin_simple2/6/log.txt"

spmdp_y1 = lr.openfile(spmdp_name1)
spmdp_y2 = lr.openfile(spmdp_name2)
spmdp_y3 = lr.openfile(spmdp_name3)
spmdp_y4 = lr.openfile(spmdp_name4)
spmdp_y5 = lr.openfile(spmdp_name5)
spmdp_y6 = lr.openfile(spmdp_name6)

x = np.array(range(40))

plt.figure(figsize=(20, 10), dpi=100)
plt.xlabel("episodes")
plt.ylabel("expected values")
plt.plot(x * 100, spmdp_y1[:40], label = "Q-Learning", color = "r")
plt.plot(x * 100, spmdp_y2[:40], label = "DDQN", color = "b")
plt.plot(x * 100, spmdp_y3[:40], label = "Maxmin N = 2", color = "green")
plt.plot(x * 100, spmdp_y4[:40], label = "Averaged N = 2", color = "y")
plt.plot(x * 100, spmdp_y5[:40], label = "Maxmin N = 4", color = "pink")
plt.plot(x * 100, spmdp_y6[:40], label = "Averaged N = 4", color = "orange")

plt.legend()
plt.show()

spmdp_name1 = "./logs/Maxmin_Mountaincar/1/log.txt"
spmdp_name2 = "./logs/Maxmin_Mountaincar/2/log.txt"
spmdp_name3 = "./logs/Maxmin_Mountaincar/3/log.txt"
spmdp_name4 = "./logs/Maxmin_Mountaincar/4/log.txt"

spmdp_y1 = lr.openfile(spmdp_name1)
spmdp_y2 = lr.openfile(spmdp_name2)
spmdp_y3 = lr.openfile(spmdp_name3)
spmdp_y4 = lr.openfile(spmdp_name4)

x = np.array(range(19))

plt.figure(figsize=(20, 10), dpi=100)
plt.xlabel("episodes")
plt.ylabel("average steps")
plt.plot(x * 100, -spmdp_y1[:19], label = "Q-Learning", color = "r")
plt.plot(x * 100, -spmdp_y2[:19], label = "DDQN", color = "b")
plt.plot(x * 100, -spmdp_y3[:19], label = "Maxmin N = 2", color = "green")
plt.plot(x * 100, -spmdp_y4[:19], label = "Averaged N = 2", color = "y")

plt.legend()
plt.show()

spmdp_name1 = "./logs/Maxmin_Lunar/1/log.txt"
spmdp_name2 = "./logs/Maxmin_Lunar/2/log.txt"
spmdp_name3 = "./logs/Maxmin_Lunar/3/log.txt"
spmdp_name4 = "./logs/Maxmin_Lunar/4/log.txt"

spmdp_y1 = lr.openfile(spmdp_name1)
spmdp_y2 = lr.openfile(spmdp_name2)
spmdp_y3 = lr.openfile(spmdp_name3)
spmdp_y4 = lr.openfile(spmdp_name4)

ran = 40
x = np.array(range(ran))

plt.figure(figsize=(20, 10), dpi=100)
plt.xlabel("episodes")
plt.ylabel("average steps")
plt.plot(x * 100, -spmdp_y1[:ran], label = "Q-Learning", color = "r")
plt.plot(x * 100, -spmdp_y2[:ran], label = "DDQN", color = "b")
plt.plot(x * 100, -spmdp_y3[:ran], label = "Maxmin N = 2", color = "green")
plt.plot(x * 100, -spmdp_y4[:ran], label = "Averaged N = 2", color = "y")

plt.legend()
plt.show()