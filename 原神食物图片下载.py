# python3
# coding: utf-8

import re
import requests
from bs4 import BeautifulSoup
import os

# 创建保存图片的文件夹
save_folder = r"D:\Users\27432\Downloads\lhcbot\1"
os.makedirs(save_folder, exist_ok=True)

html = """
                        <a href="/wiki/yuanshen/sp1.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的渔人吐司">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/55CCA2F4.jpg" alt="">
                            <span>奇怪的渔人吐司</span>
                        </a>
                        <a href="/wiki/yuanshen/sp12.html" class="list-a list-li" data-xingji="★★" data-search="莲子禽蛋羹">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/88C67B29.jpg" alt="">
                            <span>莲子禽蛋羹</span>
                        </a>
                        <a href="/wiki/yuanshen/sp11.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的莲子禽蛋羹">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/883725AE.jpg" alt="">
                            <span>奇怪的莲子禽蛋羹</span>
                        </a>
                        <a href="/wiki/yuanshen/sp10.html" class="list-a list-li" data-xingji="★★" data-search="美味的满足沙拉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/EBD65219.jpg" alt="">
                            <span>美味的满足沙拉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp9.html" class="list-a list-li" data-xingji="★★" data-search="满足沙拉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/2A6746F0.jpg" alt="">
                            <span>满足沙拉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp8.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的满足沙拉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/2A745D0C.jpg" alt="">
                            <span>奇怪的满足沙拉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp7.html" class="list-a list-li" data-xingji="★★" data-search="美味的炸萝卜丸子">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/89352FD4.jpg" alt="">
                            <span>美味的炸萝卜丸子</span>
                        </a>
                        <a href="/wiki/yuanshen/sp6.html" class="list-a list-li" data-xingji="★★" data-search="炸萝卜丸子">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/9711625B.jpg" alt="">
                            <span>炸萝卜丸子</span>
                        </a>
                        <a href="/wiki/yuanshen/sp5.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的炸萝卜丸子">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/59517ACA.jpg" alt="">
                            <span>奇怪的炸萝卜丸子</span>
                        </a>
                        <a href="/wiki/yuanshen/sp4.html" class="list-a list-li" data-xingji="★★" data-search="鱼香吐司">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/8C543F23.jpg" alt="">
                            <span>鱼香吐司</span>
                        </a>
                        <a href="/wiki/yuanshen/sp3.html" class="list-a list-li" data-xingji="★★" data-search="美味的渔人吐司">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/CF64A5F5.jpg" alt="">
                            <span>美味的渔人吐司</span>
                        </a>
                        <a href="/wiki/yuanshen/sp2.html" class="list-a list-li" data-xingji="★★" data-search="渔人吐司">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/18781EFC.jpg" alt="">
                            <span>渔人吐司</span>
                        </a>
                        <a href="/wiki/yuanshen/sp32.html" class="list-a list-li" data-xingji="★★★" data-search="美味的中原杂碎">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/71A69CC4.jpg" alt="">
                            <span>美味的中原杂碎</span>
                        </a>
                        <a href="/wiki/yuanshen/sp31.html" class="list-a list-li" data-xingji="★★★" data-search="中原杂碎">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/72706169.jpg" alt="">
                            <span>中原杂碎</span>
                        </a>
                        <a href="/wiki/yuanshen/sp30.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的中原杂碎">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/4DEFDF96.jpg" alt="">
                            <span>奇怪的中原杂碎</span>
                        </a>
                        <a href="/wiki/yuanshen/sp29.html" class="list-a list-li" data-xingji="★★★" data-search="美味的黄油松茸">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/6F266FF8.jpg" alt="">
                            <span>美味的黄油松茸</span>
                        </a>
                        <a href="/wiki/yuanshen/sp28.html" class="list-a list-li" data-xingji="★★★" data-search="黄油松茸">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/3FA5E352.jpg" alt="">
                            <span>黄油松茸</span>
                        </a>
                        <a href="/wiki/yuanshen/sp33.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的轻策农家菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/30E77DAD.jpg" alt="">
                            <span>奇怪的轻策农家菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp34.html" class="list-a list-li" data-xingji="★★★" data-search="轻策农家菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/A961695D.jpg" alt="">
                            <span>轻策农家菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp35.html" class="list-a list-li" data-xingji="★★★" data-search="美味的轻策农家菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/11A2EC09.jpg" alt="">
                            <span>美味的轻策农家菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp36.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的北地烟熏鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/CB511752.jpg" alt="">
                            <span>奇怪的北地烟熏鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp37.html" class="list-a list-li" data-xingji="★★" data-search="北地烟熏鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/08F41CD9.jpg" alt="">
                            <span>北地烟熏鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp38.html" class="list-a list-li" data-xingji="★★" data-search="美味的北地烟熏鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/5C49C581.jpg" alt="">
                            <span>美味的北地烟熏鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp39.html" class="list-a list-li" data-xingji="★" data-search="奇怪的烤肉排">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/286BE55E.jpg" alt="">
                            <span>奇怪的烤肉排</span>
                        </a>
                        <a href="/wiki/yuanshen/sp27.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的黄油松茸">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/85D2A721.jpg" alt="">
                            <span>奇怪的黄油松茸</span>
                        </a>
                        <a href="/wiki/yuanshen/sp26.html" class="list-a list-li" data-xingji="★★★" data-search="美味的来来菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/FF83E601.jpg" alt="">
                            <span>美味的来来菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp25.html" class="list-a list-li" data-xingji="★★★" data-search="来来菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/420EC277.jpg" alt="">
                            <span>来来菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp13.html" class="list-a list-li" data-xingji="★★" data-search="美味的莲子禽蛋羹
">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/FE1B0561.jpg" alt="">
                            <span>美味的莲子禽蛋羹
</span>
                        </a>
                        <a href="/wiki/yuanshen/sp14.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的香嫩椒椒鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/A689FFCB.jpg" alt="">
                            <span>奇怪的香嫩椒椒鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp15.html" class="list-a list-li" data-xingji="★★" data-search="香嫩椒椒鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/FD6BCD87.jpg" alt="">
                            <span>香嫩椒椒鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp16.html" class="list-a list-li" data-xingji="★★" data-search="美味的香嫩椒椒鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/3D20475C.jpg" alt="">
                            <span>美味的香嫩椒椒鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp17.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的白汁时蔬烩肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/86ADC831.jpg" alt="">
                            <span>奇怪的白汁时蔬烩肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp18.html" class="list-a list-li" data-xingji="★★" data-search="白汁时蔬烩肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/8FA6E501.jpg" alt="">
                            <span>白汁时蔬烩肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp19.html" class="list-a list-li" data-xingji="★★" data-search="美味的白汁时蔬烩肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/55127A51.jpg" alt="">
                            <span>美味的白汁时蔬烩肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp24.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的来来菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/504F4B31.jpg" alt="">
                            <span>奇怪的来来菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp23.html" class="list-a list-li" data-xingji="★★" data-search="美味的珍珠翡翠白玉汤">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/6E342342.jpg" alt="">
                            <span>美味的珍珠翡翠白玉汤</span>
                        </a>
                        <a href="/wiki/yuanshen/sp22.html" class="list-a list-li" data-xingji="★★" data-search="珍珠翡翠白玉汤">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/DC415C39.jpg" alt="">
                            <span>珍珠翡翠白玉汤</span>
                        </a>
                        <a href="/wiki/yuanshen/sp21.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的珍珠翡翠白玉汤">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/8682C299.jpg" alt="">
                            <span>奇怪的珍珠翡翠白玉汤</span>
                        </a>
                        <a href="/wiki/yuanshen/sp20.html" class="list-a list-li" data-xingji="★★" data-search="辣味时蔬烩肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/D9CE256B.jpg" alt="">
                            <span>辣味时蔬烩肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp53.html" class="list-a list-li" data-xingji="★" data-search="炝炒肉片">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/4808FD43.jpg" alt="">
                            <span>炝炒肉片</span>
                        </a>
                        <a href="/wiki/yuanshen/sp54.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的金丝虾球">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/902660FB.jpg" alt="">
                            <span>奇怪的金丝虾球</span>
                        </a>
                        <a href="/wiki/yuanshen/sp55.html" class="list-a list-li" data-xingji="★★" data-search="金丝虾球">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/59F24ED1.jpg" alt="">
                            <span>金丝虾球</span>
                        </a>
                        <a href="/wiki/yuanshen/sp56.html" class="list-a list-li" data-xingji="★★" data-search="美味的金丝虾球">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/2004AFCC.jpg" alt="">
                            <span>美味的金丝虾球</span>
                        </a>
                        <a href="/wiki/yuanshen/sp57.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的庄园烤松饼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/007D2AFC.jpg" alt="">
                            <span>奇怪的庄园烤松饼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp58.html" class="list-a list-li" data-xingji="★★" data-search="庄园烤松饼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/5F18759D.jpg" alt="">
                            <span>庄园烤松饼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp59.html" class="list-a list-li" data-xingji="★★" data-search="美味的庄园烤松饼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/A4D66477.jpg" alt="">
                            <span>美味的庄园烤松饼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp60.html" class="list-a list-li" data-xingji="★★" data-search="厚云朵松饼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/306D91FB.jpg" alt="">
                            <span>厚云朵松饼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp61.html" class="list-a list-li" data-xingji="★" data-search="奇怪的提瓦特煎蛋">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/E9C2ACBC.jpg" alt="">
                            <span>奇怪的提瓦特煎蛋</span>
                        </a>
                        <a href="/wiki/yuanshen/sp62.html" class="list-a list-li" data-xingji="★" data-search="提瓦特煎蛋">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/9874A012.jpg" alt="">
                            <span>提瓦特煎蛋</span>
                        </a>
                        <a href="/wiki/yuanshen/sp63.html" class="list-a list-li" data-xingji="★" data-search="美味的提瓦特煎蛋">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/95B15568.jpg" alt="">
                            <span>美味的提瓦特煎蛋</span>
                        </a>
                        <a href="/wiki/yuanshen/sp52.html" class="list-a list-li" data-xingji="★" data-search="美味的爆炒肉片">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/FAF2453F.jpg" alt="">
                            <span>美味的爆炒肉片</span>
                        </a>
                        <a href="/wiki/yuanshen/sp51.html" class="list-a list-li" data-xingji="★" data-search="爆炒肉片">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/FF91E247.jpg" alt="">
                            <span>爆炒肉片</span>
                        </a>
                        <a href="/wiki/yuanshen/sp40.html" class="list-a list-li" data-xingji="★" data-search="烤肉排">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/5026565F.jpg" alt="">
                            <span>烤肉排</span>
                        </a>
                        <a href="/wiki/yuanshen/sp41.html" class="list-a list-li" data-xingji="★" data-search="美味的烤肉排">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/4583A62C.jpg" alt="">
                            <span>美味的烤肉排</span>
                        </a>
                        <a href="/wiki/yuanshen/sp42.html" class="list-a list-li" data-xingji="★" data-search="侦察骑士烤肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/CADC5FA1.jpg" alt="">
                            <span>侦察骑士烤肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp43.html" class="list-a list-li" data-xingji="★" data-search="奇怪的摩拉肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/42DF6DBC.jpg" alt="">
                            <span>奇怪的摩拉肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp44.html" class="list-a list-li" data-xingji="★" data-search="摩拉肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/FFB666C7.jpg" alt="">
                            <span>摩拉肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp45.html" class="list-a list-li" data-xingji="★" data-search="美味的摩拉肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/05335362.jpg" alt="">
                            <span>美味的摩拉肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp46.html" class="list-a list-li" data-xingji="★" data-search="乾坤摩拉肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/CB31C0E8.jpg" alt="">
                            <span>乾坤摩拉肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp47.html" class="list-a list-li" data-xingji="★" data-search="奇怪的蒙德烤鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/222CC6F1.jpg" alt="">
                            <span>奇怪的蒙德烤鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp48.html" class="list-a list-li" data-xingji="★" data-search="蒙德烤鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/A973EF8C.jpg" alt="">
                            <span>蒙德烤鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp49.html" class="list-a list-li" data-xingji="★" data-search="美味的蒙德烤鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/57613B7C.jpg" alt="">
                            <span>美味的蒙德烤鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp50.html" class="list-a list-li" data-xingji="★" data-search="奇怪的爆炒肉片">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/8EF49D4B.jpg" alt="">
                            <span>奇怪的爆炒肉片</span>
                        </a>
                        <a href="/wiki/yuanshen/sp80.html" class="list-a list-li" data-xingji="★★" data-search="甜甜花酿鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/39E0F019.jpg" alt="">
                            <span>甜甜花酿鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp79.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的甜甜花酿鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/3CA19616.jpg" alt="">
                            <span>奇怪的甜甜花酿鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp78.html" class="list-a list-li" data-xingji="★★" data-search="美味的松茸酿肉卷">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/D0B7FC88.jpg" alt="">
                            <span>美味的松茸酿肉卷</span>
                        </a>
                        <a href="/wiki/yuanshen/sp77.html" class="list-a list-li" data-xingji="★★" data-search="松茸酿肉卷">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/9AF4CE29.jpg" alt="">
                            <span>松茸酿肉卷</span>
                        </a>
                        <a href="/wiki/yuanshen/sp81.html" class="list-a list-li" data-xingji="★★" data-search="美味的甜甜花酿鸡">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/4F864FEE.jpg" alt="">
                            <span>美味的甜甜花酿鸡</span>
                        </a>
                        <a href="/wiki/yuanshen/sp82.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的水晶虾">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/5977E383.jpg" alt="">
                            <span>奇怪的水晶虾</span>
                        </a>
                        <a href="/wiki/yuanshen/sp83.html" class="list-a list-li" data-xingji="★★" data-search="水晶虾">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/B7210504.jpg" alt="">
                            <span>水晶虾</span>
                        </a>
                        <a href="/wiki/yuanshen/sp84.html" class="list-a list-li" data-xingji="★★" data-search="美味的水晶虾">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/F6C395E9.jpg" alt="">
                            <span>美味的水晶虾</span>
                        </a>
                        <a href="/wiki/yuanshen/sp85.html" class="list-a list-li" data-xingji="★" data-search="奇怪的萝卜时蔬汤">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/4EFAE8AF.jpg" alt="">
                            <span>奇怪的萝卜时蔬汤</span>
                        </a>
                        <a href="/wiki/yuanshen/sp86.html" class="list-a list-li" data-xingji="★" data-search="萝卜时蔬汤">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/B7708CCE.jpg" alt="">
                            <span>萝卜时蔬汤</span>
                        </a>
                        <a href="/wiki/yuanshen/sp76.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的松茸酿肉卷">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/A8F18675.jpg" alt="">
                            <span>奇怪的松茸酿肉卷</span>
                        </a>
                        <a href="/wiki/yuanshen/sp75.html" class="list-a list-li" data-xingji="★★" data-search="魔法肉酱面">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/81F056DA.jpg" alt="">
                            <span>魔法肉酱面</span>
                        </a>
                        <a href="/wiki/yuanshen/sp74.html" class="list-a list-li" data-xingji="★★" data-search="美味的火火肉酱面">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/72748498.jpg" alt="">
                            <span>美味的火火肉酱面</span>
                        </a>
                        <a href="/wiki/yuanshen/sp64.html" class="list-a list-li" data-xingji="★" data-search="提瓦特焦蛋">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/55F88F51.jpg" alt="">
                            <span>提瓦特焦蛋</span>
                        </a>
                        <a href="/wiki/yuanshen/sp65.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的烤蘑菇披萨">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/79E3FC04.jpg" alt="">
                            <span>奇怪的烤蘑菇披萨</span>
                        </a>
                        <a href="/wiki/yuanshen/sp66.html" class="list-a list-li" data-xingji="★★★" data-search="烤蘑菇披萨">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/584BD814.jpg" alt="">
                            <span>烤蘑菇披萨</span>
                        </a>
                        <a href="/wiki/yuanshen/sp67.html" class="list-a list-li" data-xingji="★★★" data-search="美味的烤蘑菇披萨">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/905A8E61.jpg" alt="">
                            <span>美味的烤蘑菇披萨</span>
                        </a>
                        <a href="/wiki/yuanshen/sp68.html" class="list-a list-li" data-xingji="★★★" data-search="美味的烤蘑菇披萨">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/45264AEF.jpg" alt="">
                            <span>美味的烤蘑菇披萨</span>
                        </a>
                        <a href="/wiki/yuanshen/sp69.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的松鼠鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/464FB38D.jpg" alt="">
                            <span>奇怪的松鼠鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp70.html" class="list-a list-li" data-xingji="★★★" data-search="松鼠鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/7C3E5751.jpg" alt="">
                            <span>松鼠鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp71.html" class="list-a list-li" data-xingji="★★★" data-search="美味的松鼠鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/4C91AF45.jpg" alt="">
                            <span>美味的松鼠鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp72.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的火火肉酱面">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/3EEA6511.jpg" alt="">
                            <span>奇怪的火火肉酱面</span>
                        </a>
                        <a href="/wiki/yuanshen/sp73.html" class="list-a list-li" data-xingji="★★" data-search="火火肉酱面">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200902/0F63F30E.jpg" alt="">
                            <span>火火肉酱面</span>
                        </a>
                        <a href="/wiki/yuanshen/sp103.html" class="list-a list-li" data-xingji="★★★" data-search="蜜酱胡萝卜煎肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/0A384895.jpg" alt="">
                            <span>蜜酱胡萝卜煎肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp102.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的蜜酱胡萝卜煎肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/38B4AD86.jpg" alt="">
                            <span>奇怪的蜜酱胡萝卜煎肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp101.html" class="list-a list-li" data-xingji="★★★" data-search="真*风神杂烩菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/814003A3.jpg" alt="">
                            <span>真*风神杂烩菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp100.html" class="list-a list-li" data-xingji="★★★" data-search="美味的风神杂烩菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/3BD971A9.jpg" alt="">
                            <span>美味的风神杂烩菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp104.html" class="list-a list-li" data-xingji="★★★" data-search="美味的蜜酱胡萝卜煎肉">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/BE3EF25C.jpg" alt="">
                            <span>美味的蜜酱胡萝卜煎肉</span>
                        </a>
                        <a href="/wiki/yuanshen/sp105.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的堆高高">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/70BB6154.jpg" alt="">
                            <span>奇怪的堆高高</span>
                        </a>
                        <a href="/wiki/yuanshen/sp106.html" class="list-a list-li" data-xingji="★★★" data-search="堆高高">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/DBAFD58A.jpg" alt="">
                            <span>堆高高</span>
                        </a>
                        <a href="/wiki/yuanshen/sp107.html" class="list-a list-li" data-xingji="★★★" data-search="美味的堆高高">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/B2106932.jpg" alt="">
                            <span>美味的堆高高</span>
                        </a>
                        <a href="/wiki/yuanshen/sp108.html" class="list-a list-li" data-xingji="★★★" data-search="蒙德往事">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/C8B667FC.jpg" alt="">
                            <span>蒙德往事</span>
                        </a>
                        <a href="/wiki/yuanshen/sp109.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的冷肉拼盘
">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/1937BE60.jpg" alt="">
                            <span>奇怪的冷肉拼盘
</span>
                        </a>
                        <a href="/wiki/yuanshen/sp99.html" class="list-a list-li" data-xingji="★★★" data-search="风神杂烩菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/C4C67AA0.jpg" alt="">
                            <span>风神杂烩菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp98.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的风神杂烩菜">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/E5C21A0B.jpg" alt="">
                            <span>奇怪的风神杂烩菜</span>
                        </a>
                        <a href="/wiki/yuanshen/sp97.html" class="list-a list-li" data-xingji="★" data-search="美味的烤吃虎鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/7721F58C.jpg" alt="">
                            <span>美味的烤吃虎鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp87.html" class="list-a list-li" data-xingji="★" data-search="美味的萝卜时蔬汤">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/1F245FA2.jpg" alt="">
                            <span>美味的萝卜时蔬汤</span>
                        </a>
                        <a href="/wiki/yuanshen/sp88.html" class="list-a list-li" data-xingji="★" data-search="奇怪的野菇鸡肉串">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/9ED375B0.jpg" alt="">
                            <span>奇怪的野菇鸡肉串</span>
                        </a>
                        <a href="/wiki/yuanshen/sp89.html" class="list-a list-li" data-xingji="★" data-search="野菇鸡肉串">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/9D02C65E.jpg" alt="">
                            <span>野菇鸡肉串</span>
                        </a>
                        <a href="/wiki/yuanshen/sp90.html" class="list-a list-li" data-xingji="★" data-search="美味的野菇鸡肉串">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/5BA2893D.jpg" alt="">
                            <span>美味的野菇鸡肉串</span>
                        </a>
                        <a href="/wiki/yuanshen/sp91.html" class="list-a list-li" data-xingji="★" data-search="果香串烤">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/A556E6D7.jpg" alt="">
                            <span>果香串烤</span>
                        </a>
                        <a href="/wiki/yuanshen/sp92.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的嘟嘟莲海鲜羹">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/28701927.jpg" alt="">
                            <span>奇怪的嘟嘟莲海鲜羹</span>
                        </a>
                        <a href="/wiki/yuanshen/sp93.html" class="list-a list-li" data-xingji="★★★" data-search="嘟嘟莲海鲜羹">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/D843572C.jpg" alt="">
                            <span>嘟嘟莲海鲜羹</span>
                        </a>
                        <a href="/wiki/yuanshen/sp94.html" class="list-a list-li" data-xingji="★★★" data-search="美味的嘟嘟莲海鲜羹">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/FA7DECB9.jpg" alt="">
                            <span>美味的嘟嘟莲海鲜羹</span>
                        </a>
                        <a href="/wiki/yuanshen/sp95.html" class="list-a list-li" data-xingji="★" data-search="奇怪的烤吃虎鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/DEF1FF8D.jpg" alt="">
                            <span>奇怪的烤吃虎鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp96.html" class="list-a list-li" data-xingji="★" data-search="烤吃虎鱼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/D9F9431D.jpg" alt="">
                            <span>烤吃虎鱼</span>
                        </a>
                        <a href="/wiki/yuanshen/sp119.html" class="list-a list-li" data-xingji="★★★" data-search="奇怪的蟹黄火腿焗时蔬">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/F25BC59D.jpg" alt="">
                            <span>奇怪的蟹黄火腿焗时蔬</span>
                        </a>
                        <a href="/wiki/yuanshen/sp120.html" class="list-a list-li" data-xingji="★★★" data-search="蟹黄火腿焗时蔬">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/7B4C4603.jpg" alt="">
                            <span>蟹黄火腿焗时蔬</span>
                        </a>
                        <a href="/wiki/yuanshen/sp121.html" class="list-a list-li" data-xingji="★★★" data-search="美味的蟹黄火腿焗时蔬">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/2CBF8C8A.jpg" alt="">
                            <span>美味的蟹黄火腿焗时蔬</span>
                        </a>
                        <a href="/wiki/yuanshen/sp122.html" class="list-a list-li" data-xingji="★★★★★" data-search="奇怪的仙跳墙">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/EFCD51C6.jpg" alt="">
                            <span>奇怪的仙跳墙</span>
                        </a>
                        <a href="/wiki/yuanshen/sp123.html" class="list-a list-li" data-xingji="★★★★★" data-search="仙跳墙">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/EFCD51C6.jpg" alt="">
                            <span>仙跳墙</span>
                        </a>
                        <a href="/wiki/yuanshen/sp124.html" class="list-a list-li" data-xingji="★★★★★" data-search="美味的仙跳墙">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/216C30D8.jpg" alt="">
                            <span>美味的仙跳墙</span>
                        </a>
                        <a href="/wiki/yuanshen/sp118.html" class="list-a list-li" data-xingji="★★" data-search="美味的杏仁豆腐">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/5F13A9DC.jpg" alt="">
                            <span>美味的杏仁豆腐</span>
                        </a>
                        <a href="/wiki/yuanshen/sp117.html" class="list-a list-li" data-xingji="★★" data-search="杏仁豆腐">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/83ADDCD1.jpg" alt="">
                            <span>杏仁豆腐</span>
                        </a>
                        <a href="/wiki/yuanshen/sp116.html" class="list-a list-li" data-xingji="★★" data-search="奇怪的杏仁豆腐">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/025CC9EF.jpg" alt="">
                            <span>奇怪的杏仁豆腐</span>
                        </a>
                        <a href="/wiki/yuanshen/sp115.html" class="list-a list-li" data-xingji="★★★★" data-search="美味的翡玉什锦袋">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/9B1483C0.jpg" alt="">
                            <span>美味的翡玉什锦袋</span>
                        </a>
                        <a href="/wiki/yuanshen/sp114.html" class="list-a list-li" data-xingji="★★★★" data-search="翡玉什锦袋">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/7439B97B.jpg" alt="">
                            <span>翡玉什锦袋</span>
                        </a>
                        <a href="/wiki/yuanshen/sp113.html" class="list-a list-li" data-xingji="★★★★" data-search="奇怪的翡玉什锦袋">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/FF4665A0.jpg" alt="">
                            <span>奇怪的翡玉什锦袋</span>
                        </a>
                        <a href="/wiki/yuanshen/sp112.html" class="list-a list-li" data-xingji="★★★" data-search="祝圣交响乐">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/559677FF.jpg" alt="">
                            <span>祝圣交响乐</span>
                        </a>
                        <a href="/wiki/yuanshen/sp111.html" class="list-a list-li" data-xingji="★★★" data-search="美味的冷肉拼盘">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/02ADC655.jpg" alt="">
                            <span>美味的冷肉拼盘</span>
                        </a>
                        <a href="/wiki/yuanshen/sp110.html" class="list-a list-li" data-xingji="★★★" data-search="冷肉拼盘">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/F2476E4D.jpg" alt="">
                            <span>冷肉拼盘</span>
                        </a>
                        <a href="/wiki/yuanshen/sp125.html" class="list-a list-li" data-xingji="★★★" data-search="蒙德土豆饼">
                            <img class="lazy" data-original="//img1.ali213.net/glpic/upload/20200903/94AF1C97.jpg" alt="">
                            <span>蒙德土豆饼</span>
                        </a>
"""

# 解析HTML
soup = BeautifulSoup(html, "html.parser")

# 找到所有的a标签
a_tags = soup.find_all("a")

# 用于处理非法字符的正则表达式，将非法字符替换为空格
illegal_char_regex = re.compile(r'[\\/:"*?<>|]')

for a_tag in a_tags:
    # 找到对应的图片链接和食物名称
    img_tag = a_tag.find("img")
    img_link = img_tag["data-original"]
    food_name = a_tag.find("span").text.strip()

    # 检查链接是否包含了合适的scheme
    if not img_link.startswith("http"):
        img_link = "http:" + img_link

    # 下载图片
    image_data = requests.get(img_link).content

    # 替换非法字符为空格
    food_name = re.sub(illegal_char_regex, ' ', food_name)

    # 构建图片保存路径
    img_filename = f"{food_name}.jpg"
    img_path = os.path.join(save_folder, img_filename)

    # 保存图片
    with open(img_path, "wb") as img_file:
        img_file.write(image_data)