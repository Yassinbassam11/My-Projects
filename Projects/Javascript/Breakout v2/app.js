const board = document.querySelector('#board')
const scoreDisplay = document.querySelector('#score')
const boardWidth = 560
const boardHeight = 300
const blockWidth = 100
const blockHeight = 20
const ballDiameter = 20
const numOfBlocks = 15
const blocksCoordinate = []
let userCoordinate = [230,10]
let ballCoordinate = [270,40]
let x_movement = 2
let y_movement = 2
let user_movement = 10
let ballMoveTimer
let topWallCollisionFlag = false
let userCollisionFlag = false
let score = 0
// let leftWallCollisionFlag = false
// let rightWallCollisionFlag = false

function createBlocks(){
    let x = 0
    let y = 270
    for(let i=0;i<numOfBlocks;i++){
        x +=10
        const block = document.createElement('div')
        block.classList.add('block')
        block.style.left = x +'px'
        block.style.bottom = y + 'px'
        blocksCoordinate.push([x,y])
        board.appendChild(block)
        x += blockWidth
        if(x==550){
            y -= (10+blockHeight)
            x =0
        }
    }
}
createBlocks()

const userBlock = document.createElement('div')
function createUser(){
    userBlock.style.left = userCoordinate[0] +'px'
    userBlock.style.bottom = userCoordinate[1] +'px'
    userBlock.classList.add('userBlock')
    board.appendChild(userBlock)
}
createUser()

const ball = document.createElement('div')
function createBall(){
    ball.style.left = ballCoordinate[0] + 'px'
    ball.style.bottom = ballCoordinate[1] + 'px'
    ball.classList.add('ball')
    board.appendChild(ball)
}
createBall()

function updateBallPosition(){
    ball.style.left = ballCoordinate[0] + 'px'
    ball.style.bottom = ballCoordinate[1] + 'px'
}

function updateUserPosition(){
    userBlock.style.left = userCoordinate[0] + 'px'
    userBlock.style.bottom = userCoordinate[1] + 'px'
}

function moveBall(){
    ballCoordinate[0] += x_movement
    ballCoordinate[1] += y_movement
    updateBallPosition()
    checkCollision()
}
ballMoveTimer = setInterval(moveBall,20)

function moveUser(e){
    if(e.key == 'ArrowLeft'){
        if(userCoordinate[0]>0){
            userCoordinate[0] -= user_movement
            updateUserPosition()
        }
    }
    else if(e.key == 'ArrowRight'){
        if(userCoordinate[0]<boardWidth-blockWidth){
            userCoordinate[0] += user_movement
            updateUserPosition()
        }
    }
}
document.addEventListener('keydown',moveUser)

function checkCollision(){
    for(let i=0;i<blocksCoordinate.length;i++){
        if((ballCoordinate[0]>blocksCoordinate[i][0] && ballCoordinate[0]<blocksCoordinate[i][0]+blockWidth) &&
        (ballCoordinate[1]>blocksCoordinate[i][1] && ballCoordinate[1]<blocksCoordinate[i][1]+blockHeight)){
            const blocks = Array.from(document.querySelectorAll('.block'))
            blocks[i].classList.remove('block')
            blocksCoordinate.splice(i,1)
            topWallCollisionFlag = true
            changeDirection()
            score++
            scoreDisplay.innerHTML = score
            if(blocksCoordinate.length == 0){
                scoreDisplay.innerHTML = score + ' (You Win)'
                clearInterval(ballMoveTimer)
                document.removeEventListener('keydown',moveUser)
            }
        }
    }
    if(ballCoordinate[0]<=0 || ballCoordinate[0]+ballDiameter>=boardWidth){
        changeDirection()
    }
    else if(ballCoordinate[1]+ballDiameter>=boardHeight){
        topWallCollisionFlag = true
        changeDirection()
    }
    else if(ballCoordinate[1]<0){
        clearInterval(ballMoveTimer)
        scoreDisplay.innerHTML = score + ' (You Lose)'
        document.removeEventListener('keydown',moveUser)
    }
    else if((ballCoordinate[0]>userCoordinate[0] && ballCoordinate[0]<userCoordinate[0]+blockWidth) &&
    (ballCoordinate[1]>userCoordinate[1] && ballCoordinate[1]<userCoordinate[1]+blockHeight)){
        userCollisionFlag =true
        changeDirection()
    }
}

function changeDirection(){
    if(topWallCollisionFlag ==true){
        if(x_movement>0 && y_movement>0){
            y_movement *= -1
        }
        else if(x_movement<0 && y_movement>0){
            y_movement *= -1
        }
        topWallCollisionFlag =false
    }
    else if(userCollisionFlag == true){
        if(x_movement<0 && y_movement<0){y_movement *= -1}
        else if(x_movement>0 && y_movement<0){y_movement *= -1}
        userCollisionFlag =false
    }
    else if(x_movement>0 && y_movement>0){x_movement *= -1}
    else if(x_movement<0 && y_movement>0){x_movement *= -1}
    else if(x_movement<0 && y_movement<0){x_movement *= -1}
    else if(x_movement>0 && y_movement<0){x_movement *= -1}
    else{
        x_movement = 0
        y_movement = 0
    }
}
// function changeDirection(){
//     if (x_movement === 2 && y_movement === 2) {
//         y_movement = -2
//         return
//       }
//       if (x_movement === 2 && y_movement === -2) {
//         x_movement = -2
//         return
//       }
//       if (x_movement === -2 && y_movement === -2) {
//         y_movement = 2
//         return
//       }
//       if (x_movement === -2 && y_movement === 2) {
//         x_movement = 2
//         return
//       }
// }


// console.log(blocksCoordinate)
// // blocksCoordinate[0].splice(0,2)
// blocksCoordinate.splice(0,1)
// // console.log(blocksCoordinate)