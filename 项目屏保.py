import random
import tkinter


class RandomBall():
    '''
    定义球的运动的类
    '''

    def __init__(self, canvas, scrnwidth, scrnheight):
        '''
        candvass:画布，所有的内容都应该在画布上呈现
        通过变量scrnwidth,scrnheight:屏幕宽高
        '''
        # 球出现的位置要随机
        self.xpos = random.randint(10, int(scrnwidth) - 20)
        self.ypos = random.randint(10, int(scrnheight) - 20)

        self.canvas = canvas
        # 定义球运动的速度
        # 模拟运动：不断的擦除原来的画，然后在一个新的地方从新绘制
        self.xvelocity = random.randint(4, 30)
        self.yvelocity = random.randint(4, 30)
        # 定义屏幕大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        # 定义球的大随机大小
        self.radius = random.randint(20, 50)
        # 定义颜色
        # RGB ：三个数字（红绿蓝）0-255
        # 在某些系统里，直接用英文表示也可以
        # 此处用lambda表示
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def create_ball(self):
            '''
            用构造函数定义变量的值，在canvas上画一个球
            '''
            # tkinter没有画⚪函数
            # 只有一个椭圆函数，画椭圆需要定义两个坐标
            # 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就ok
            # 求两个坐标的方法，已知圆心坐标加减半径就ok了
            x1 = self.xpos - self.radius
            y1 = self.ypos - self.radius
            x2 = self.xpos + self.radius
            y2 = self.ypos + self.radius

            # 再对两个对角坐标前提下，可以进行画圆
            self.item = self.canvas.create_oval(x1, y1, x2, y2,fill=self.color,outline=self.color)

    def move_ball(self):
            # 球的移动方向，需要控制球的方向
            # 每次球都有一个新的坐标
            self.xpos += self.xvelocity
            self.ypos += self.yvelocity

            # 以下判断是否会撞墙
            # 撞墙回头
            if self.xpos + self.radius >= self.scrnwidth:
                # 撞到右墙
                if self.xvelocity >= 0:
                    self.xvelocity = -self.xvelocity
            if self.xpos - self.radius <= 0:
                if self.xvelocity <= 0:
                    self.xvelocity *= -1
            if self.ypos + self.radius >= self.scrnheight:
                if self.yvelocity >= 0:
                    self.yvelocity *= -1
            if self.ypos - self.radius <= 0:
                if self.yvelocity <= 0:
                    self.yvelocity *= -1

            # 在画布上移动
            self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver():
    '''
    定义屏保类
    可以被启动
    '''
    # 如何随机产生球
    balls = list()

    def __init__(self):
        # 每次启动球的数量是随机的
        self.num_balls = random.randint(6, 20)
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)
        # 任何鼠标移动都需要取消
        self.root.bind('<Motion>', self.myquit)
        self.root.bind('<Any-KeyPress>', self.myquit)

        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()  # 消息
        #self.root2 = tkinter.Tk()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        # after是200毫秒后启动一个函数，需要启动的函数时第二个函数
        self.canvas.after(200, self.run_screen_saver)

    def myquit(self,e):
        # 此处只是利用了事件的处理机制
        # 实际上并不关心事件的类型
        # 作业:
        # 此屏保程序扩展成，一旦捕获事件，则判断屏保不退出
        # 显示一个BUtton，button上显示事件类型，点击button后屏保
        # 才退出
        self.root.destroy()
        '''
        self.root2.wm_title('退出锁屏界面')
        def myEsc():
            self.root.destroy()
            self.root2.destroy()

        b1 = tkinter.Button(root2, text="quit the screen", command=myEsc)
        b1.pack()
        root2.mainloop()
        '''


if __name__ == "__main__":
    ss = ScreenSaver()