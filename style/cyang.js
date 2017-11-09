//存储图片地址
var imageAddress= new Array()
imageAddress[0]='image/1.png'
imageAddress[1]='image/2.png'
imageAddress[2]='image/3.png'
imageAddress[3]='image/4.png'
imageAddress[4]='image/5.png'
imageAddress[5]='image/6.png'
imageAddress[6]='image/7.png'
imageAddress[7]='image/8.png'
imageAddress[8]='image/9.png'
imageAddress[9]='image/10.png'
//修改背景图片
function  newBackgroundImage(id){
    //产生一个0－9的随机数
    var i=parseInt(Math.random()*10)
    //将id＝id的容器的背景图片地址改为imageAddress[i]
    document.getElementById(id).src=imageAddress[i]
}
