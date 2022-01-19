import turtle

## 함수 선언 부분 ## 

## 변수 선언 부분 ## 
myT = None

## 메인 코드 부분 ## 
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0, 3) :
    myT.forward(100)
    myT.right(90)
    myT.backward(200)

turtle.done()
