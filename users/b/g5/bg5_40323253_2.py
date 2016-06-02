from flask import Blueprint, request

bg5_40323253_2 = Blueprint('bg5_40323253_2', __name__, url_prefix='/bg5_40323253_2', template_folder='templates')

@bg5_40323253_2.route('/a')
def draw_a():

    outstring ='''

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">


<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/Cango2D-7v01-min.js"></script>
<script type="text/javascript" src="http://2015fallhw.github.io/cptocadp/static/gearUtils-05.js"></script>
 
<script>
window.onload=function(){
brython(1);
}
</script>
 
<div id="container"></div>
 
<script type="text/python" src="http://cadlab.mde.tw/post/by/spur.js" id="spurmain"></script>
 
<script type="text/python">
import spurmain
from browser import document, html
# 利用 Brython 的 document 建立一個 id 為 container 的 div 區域, 然後在其中放入對應的 html 標註
container = document['container']
# 3個齒輪的齒數
n1 = 17
n2 = 29
n3 = 15
# 根據繪圖的 3 個齒輪大小計算所需的畫布高度
height = 1.2*800*0.8/(int(n1)+int(n2)+int(n3))*max([int(n1), int(n2), int(n3)])
# 決定畫布的 id 字串
id = "gear"
# 利用 Brython 的 html 方法建立 CANVAS
canvas = html.CANVAS(id=id, width=800, height=height)
 
# 將所建立的 canvas 畫布標註放入 container
container <= canvas
 
# m 為模數, 根據畫布的寬度, 計算適合的模數大小
# Module = mm of pitch diameter per tooth
# 利用 80% 的畫布寬度進行繪圖
# 計算模數的對應尺寸
m = canvas.width*0.8/(n1+n2+n3)
 
# 根據齒數與模組計算各齒輪的節圓半徑
pr1 = n1*m/2
pr2 = n2*m/2
pr3 = n3*m/2
 
# 畫布左右兩側都保留畫布寬度的 10%
# 依此計算對應的最左邊齒輪的軸心座標
cx = canvas.width*0.1+pr1
cy = canvas.height/2
 
# pa 為壓力角
pa = 25
 
# 這裡的齒輪繪圖以所導入的 spurmain 模組中的 Spur 類別建立對應的 gear 變數, 且宣告畫布 id
gear = spurmain.Spur(id)
 
# 畫最左邊齒輪, 定位線旋轉角為 0, 軸心座標 (cx, cy)
gear.spur(cx, cy, m, n1, pa, 0)
# 第2個齒輪將原始的定位線逆時鐘轉 180 度後, 與第1個齒輪正好齒頂與齒頂對齊
# 只要第2個齒輪再逆時鐘或順時鐘轉動半齒的角度, 即可完成囓合
# 每一個齒分別包括從齒根到齒頂的範圍, 涵蓋角度為 360/n, 因此所謂的半齒角度為 180/n
gear.spur(cx+pr1+pr2, cy, m, n2, pa, 180-180/n2)
# 第2齒與第3齒的囓合, 首先假定第2齒的定位線在 theta 角為 0 的原始位置
# 如此, 第3齒只要逆時鐘旋轉 180 度後, 再逆時鐘或順時鐘轉動半齒的角度, 即可與第2齒囓合
# 但是第2齒為了與第一齒囓合時, 已經從原始定位線轉了 180-180/n2 度
# 而當第2齒從與第3齒囓合的定位線, 逆時鐘旋轉 180-180/n2 角度後, 原先囓合的第3齒必須要再配合旋轉 (180-180/n2 )*n2/n3
gear.spur(cx+pr1+pr2+pr2+pr3, cy, m, n3, pa, 180-180/n3+(180-180/n2)*n2/n3)
</script>
<div id="container1"></div>
 
<script type="text/python">
import spurmain
from browser import document, html
 
# 建立新的繪圖方法 sprocket 用
from browser import window
from javascript import JSConstructor
import math
 
cango = JSConstructor(window.Cango)
shapedefs = window.shapeDefs
cobj = JSConstructor(window.Cobj)
creategeartooth = JSConstructor(window.createGearTooth)
 
class mySpur(spurmain.Spur):
    # 定義 sprocket
    # rs 為 roller rasius
    # pc 為 pitch
    def sprocket(self, cx, cy, rs, pc, n, theta):
        self.cx = cx
        self.cy = cy
        self.rs = rs
        self.pc = pc
        self.n = n
        self.pa = pa
        self.theta = theta
        rotangle = 360/self.n
        pr = self.pc/2/math.sin((rotangle/2)*math.pi/180)
        pt1x = pr-rs
        pt1y = 0
        pt2x = pr-(pr-pr*math.cos(rotangle*math.pi/180))*rs/pc
        pt2y = (pr*math.sin(rotangle*math.pi/180))*rs/pc
        ptmx = pr-(pr-pr*math.cos(rotangle*math.pi/180))*(0.5*pc)/pc
        ptmy = (pr*math.sin(rotangle*math.pi/180))*(0.5*pc)/pc
        lenmto3 = math.sqrt(math.pow(pc-rs,2)-math.pow(pc*0.5, 2))
        lenztom = math.sqrt(math.pow(ptmx, 2)+math.pow(ptmy, 2))
        r3 = lenztom + lenmto3
        pt3x = r3*math.cos(0.5*rotangle*math.pi/180)
        pt3y = r3*math.sin(0.5*rotangle*math.pi/180)
        pt4x = pr-(pr-pr*math.cos(rotangle*math.pi/180))*(pc-rs)/pc
        pt4y = (pr*math.sin(rotangle*math.pi/180))*(pc-rs)/pc
        pt5x = (pr-rs)*math.cos(rotangle*math.pi/180)
        pt5y = (pr-rs)*math.sin(rotangle*math.pi/180)
        data = ['M', pt1x, pt1y, 'A', rs, rs, 0, 0, 0, pt2x, pt2y, \
        'A', pc-rs, pc-rs, 0, 0, 1, pt3x, pt3y, \
        'A', pc-rs, pc-rs, 0, 0, 1, pt4x, pt4y, \
        'A', rs, rs, 0, 0, 0, pt5x, pt5y]
        sprocketTooth = cobj(data, "SHAPE", {
                "fillColor":"#ddd0dd",
                "border": True,
                "strokeColor": "#606060" })
        # theta 為 degree
        sprocketTooth.rotate(self.theta) 
        sprocket = sprocketTooth.dup()
        # 利用單齒輪廓旋轉, 產生整個齒盤外形
        for i in range(1, self.n):
            # 將 sprocketTooth 中的資料複製到 newTooth
            newTooth = sprocketTooth.dup()
            # 配合迴圈, newTooth 的齒形資料進行旋轉, 然後利用 appendPath 方法, 將資料併入 gear
            newTooth.rotate(360*i/self.n)
            # appendPath 為 Cango 程式庫中的方法, 第二個變數為 True, 表示要刪除最前頭的 Move to SVG Path 標註符號
            sprocket.appendPath(newTooth, True) # trim move command = True
        # 建立軸孔
        # add axle hole, hr 為 hole radius
        hr = 0.6*pr # diameter of gear shaft
        shaft = cobj(shapedefs.circle(hr), "PATH")
        shaft.revWinding()
        sprocket.appendPath(shaft) # retain the 'moveTo' command for shaft sub path
        sprocket.translate(self.cx, self.cy)
        # render 繪出靜態正齒輪輪廓
        self.cgo.render(sprocket)
        # 接著繪製齒盤的基準線
        deg = math.pi/180
        Line = cobj(['M', self.cx, self.cy, 'L', self.cx+pr*math.cos(self.theta*deg), self.cy+pr*math.sin(self.theta*deg)], "PATH", {
              'strokeColor':'blue', 'lineWidth': 1})
        self.cgo.render(Line)
 
# 將繪製鏈條輪廓的內容寫成 class 物件
class Chain():
    def __init__(self, canvas_id):
        self.canvas_id = canvas_id
        self.cgo = cango(self.canvas_id)
 
    def chain(self, x, y, rs, pc, theta, render=True):
        self.x = x
        self.y = y
        self.rs = rs
        self.pc = pc
        self.theta = theta
        self.render = render
        # rs 為 roller rasius
        # pc 為 pitch
        # 以水平作為起始角度, 左邊圓心位於原點, 左右圓半徑為 rs = 7, pc 為 20, 上下圓弧半徑為 20
        cx = 0
        cy = 0
        c2x = cx + self.pc
        c2y = cy
        # upper arc center coord
        ucx = self.pc/2
        ucy = math.sqrt(math.pow(self.rs+self.pc, 2)-math.pow(0.5*self.pc, 2))
        # down side arc center coord
        dcx = ucx
        dcy = -math.sqrt(math.pow(self.rs+self.pc, 2)-math.pow(0.5*self.pc, 2))
        # 上方左邊切點座標
        pt1x = cx+(ucx-cx)*(self.rs/(self.pc+self.rs))
        pt1y = cy+(ucy-cy)*(self.rs/(self.pc+self.rs)) 
        pt2x = cx+(dcx-cx)*(self.rs/(self.pc+self.rs))
        pt2y = cy+(dcy-cy)*(self.rs/(self.pc+self.rs))
        pt3x = c2x+self.rs*(dcx-c2x)/(self.pc+self.rs)
        pt3y = c2y+self.rs*(dcy-c2y)/(self.pc+self.rs)
        pt4x = c2x+self.rs*(ucx-c2x)/(self.pc+self.rs)
        pt4y = c2y+self.rs*(ucy-c2y)/(self.pc+self.rs)
 
        # 輪廓的外型設為成員變數
        data = ['M', pt1x, pt1y, \
                'A', self.rs, self.rs, 0, 1, 1, pt2x, pt2y, \
                'A', self.pc, self.pc, 0, 0, 0, pt3x, pt3y, \
                'A', self.rs, self.rs, 0, 1, 1, pt4x, pt4y, \
                'A', self.pc, self.pc, 0, 0, 0, pt1x, pt1y, 'z']
 
        chain = cobj(data, "SHAPE", {
                "fillColor":"#ddd0dd",
                "border": True,
                "strokeColor": "#606060" })
 
        hole1 = cobj(shapedefs.circle(self.rs/1.5), "PATH")
        hole1.translate(cx, cy)
        hole1.revWinding()
        chain.appendPath(hole1)
        hole2 = cobj(shapedefs.circle(self.rs/1.5), "PATH")
        hole2.translate(c2x, c2y)
        hole2.revWinding()
        chain.appendPath(hole2)
       # theta is degree
        chain.rotate(self.theta)
        chain.translate(self.x, self.y)
        if self.render == True:
            self.cgo.render(chain)
        deg = math.pi/180
        x2 = cx + self.x+ self.pc*math.cos(self.theta*deg)
        y2 = cy + self.y+ self.pc*math.sin(self.theta*deg)
        return x2, y2
 
# 利用 Brython 的 document 建立一個 id 為 container 的 div 區域, 然後在其中放入對應的 html 標註
container = document['container1']
# 3個齒輪的齒數
n1 = 18
n2 = 29
n3 = 15
# 根據繪圖的 3 個齒輪大小計算所需的畫布高度
height = 1.2*800*0.8/(int(n1)+int(n2)+int(n3))*max([int(n1), int(n2), int(n3)])
# 決定畫布的 id 字串
id = "gear1"
# 利用 Brython 的 html 方法建立 CANVAS
canvas = html.CANVAS(id=id, width=800, height=height)
 
# 將所建立的 canvas 畫布標註放入 container
container <= canvas
 
# m 為模數, 根據畫布的寬度, 計算適合的模數大小
# Module = mm of pitch diameter per tooth
# 利用 80% 的畫布寬度進行繪圖
# 計算模數的對應尺寸
m = canvas.width*0.8/(n1+n2+n3)
 
# 根據齒數與模組計算各齒輪的節圓半徑
pr1 = n1*m/2
pr2 = n2*m/2
pr3 = n3*m/2
 
# 畫布左右兩側都保留畫布寬度的 10%
# 依此計算對應的最左邊齒輪的軸心座標
cx = canvas.width*0.1+pr1
cy = canvas.height/2
 
# pa 為壓力角
pa = 25
 
# mySpur 已經新建一個 sprocket 繪圖方法
gear = mySpur(id)
 
# 畫最左邊齒輪, 定位線旋轉角為 0, 軸心座標 (cx, cy)
gear.sprocket(cx, cy, 7, 20, n1, 0)
# 第2個齒輪將原始的定位線逆時鐘轉 180 度後, 與第1個齒輪正好齒頂與齒頂對齊
# 只要第2個齒輪再逆時鐘或順時鐘轉動半齒的角度, 即可完成囓合
# 每一個齒分別包括從齒根到齒頂的範圍, 涵蓋角度為 360/n, 因此所謂的半齒角度為 180/n
gear.sprocket(cx+pr1+pr2, cy, 7, 20, n2, 180-180/n2)
# 第2齒與第3齒的囓合, 首先假定第2齒的定位線在 theta 角為 0 的原始位置
# 如此, 第3齒只要逆時鐘旋轉 180 度後, 再逆時鐘或順時鐘轉動半齒的角度, 即可與第2齒囓合
# 但是第2齒為了與第一齒囓合時, 已經從原始定位線轉了 180-180/n2 度
# 而當第2齒從與第3齒囓合的定位線, 逆時鐘旋轉 180-180/n2 角度後, 原先囓合的第3齒必須要再配合旋轉 (180-180/n2 )*n2/n3
gear.sprocket(cx+pr1+pr2+pr2+pr3, cy, 7, 20, n3, 180-180/n3+(180-180/n2)*n2/n3)
 
rs = 7
pc = 20
degree = math.pi/180
radian = 180/math.pi
rotangle = 360/n1
r1 = pc/2/math.sin((rotangle/2)*math.pi/180)
inc = math.pi - math.atan2(r1*math.sin(rotangle*degree), r1-r1*math.cos(rotangle*degree))
mychain = Chain(id)
x1 = cx + r1
y1 = cy
for i in range(n1-5):
    if i < 5:
        x2, y2 = mychain.chain(x1, y1, rs, pc, inc*radian+rotangle*i, False)
    else:
        x2, y2 = mychain.chain(x1, y1, rs, pc, inc*radian+rotangle*i)
    x1, y1 = x2, y2
 
rotangle = 360/n2
r2 = pc/2/math.sin((rotangle/2)*math.pi/180)
inc = math.pi - math.atan2(r2*math.sin(rotangle*degree), r2-r2*math.cos(rotangle*degree))
mychain = Chain(id)
x1 = cx+pr1+pr2+r2
y1 = cy
for i in range(n2):
    if i > 7 and i < 20:
        x2, y2 = mychain.chain(x1, y1, rs, pc, inc*radian+rotangle*i, False)
    else:
        x2, y2 = mychain.chain(x1, y1, rs, pc, inc*radian+rotangle*i)
    x1, y1 = x2, y2
    if i == 7:
        x7, y7 = x2, y2
    if i == 19:
        x20, y20 = x2, y2
 
for i in range(12):
    if i == 11:
        offset = 12
    else:
        offset = 0
    x2, y2 = mychain.chain(x7, y7, rs, pc, inc*radian+rotangle*8-i*1.5+offset)
    x7, y7 = x2, y2
 
for i in range(11):
    if i == 10:
        offset = 2
    else:
        offset = 0
    x2, y2 = mychain.chain(x20, y20, rs, pc, -inc*radian+rotangle*20+20+offset)
    x20, y20 = x2, y2
</script>
'''
    return outstring