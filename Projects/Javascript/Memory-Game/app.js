const cardarray = [
    {
        name:'fries',
        img:'images/fries.png'
    },
    {
        name:'cheeseburger',
        img:'images/cheeseburger.png'
    },
    {
        name:'hotdog',
        img:'images/hotdog.png'
    },
    {
        name:'ice-cream',
        img:'images/ice-cream.png'
    },
    {
        name:'milkshake',
        img:'images/milkshake.png'
    },
    {
        name:'pizza',
        img:'images/pizza.png'
    },
    {
        name:'fries',
        img:'images/fries.png'
    },
    {
        name:'cheeseburger',
        img:'images/cheeseburger.png'
    },
    {
        name:'hotdog',
        img:'images/hotdog.png'
    },
    {
        name:'ice-cream',
        img:'images/ice-cream.png'
    },
    {
        name:'milkshake',
        img:'images/milkshake.png'
    },
    {
        name:'pizza',
        img:'images/pizza.png'
    }
]

cardarray.sort(() => Math.random()-0.5)
const gridDisplay = document.querySelector('#grid')
const resultDisplay = document.querySelector('#result')
let cardChosen = []
let cardChosenIds = []
const cardsWon = []

function createBoard(){
    for(let i=0;i<cardarray.length;i++){
        const card = document.createElement('img')
        card.setAttribute('src','images/blank.png')
        card.setAttribute('data-id',i)
        card.addEventListener('click',flipCard)
        gridDisplay.append(card)
    }
}
createBoard()

function checkMatch(){
    const cards = document.querySelectorAll('#grid img')
    console.log(cards)
    console.log("check for match!")
    if(cardChosenIds[0] == cardChosenIds[1]){
        alert("you have clicked the same image!")
        cards[cardChosenIds[0]].setAttribute('src','images/blank.png')
        cards[cardChosenIds[1]].setAttribute('src','images/blank.png')
    }
    if(cardChosen[0] == cardChosen[1]){
        alert('you found a match!')
        cards[cardChosenIds[0]].setAttribute('src','images/white.png')
        cards[cardChosenIds[1]].setAttribute('src','images/white.png')
        cards[cardChosenIds[0]].removeEventListener('click',flipCard)
        cardsWon.push(cardChosen)
    }
    else{
        cards[cardChosenIds[0]].setAttribute('src','images/blank.png')
        cards[cardChosenIds[1]].setAttribute('src','images/blank.png')
        alert('sorry try again!')
    }
    resultDisplay.innerHTML=cardsWon.length
    cardChosen = []
    cardChosenIds = []
    if(cardsWon.length == cardarray.length/2){
        resultDisplay.innerHTML = 'congratulations you found them all!'
    }
}

function flipCard(){
    const cardId = this.getAttribute('data-id')
    cardChosen.push(cardarray[cardId].name)
    cardChosenIds.push(cardId)
    this.setAttribute('src',cardarray[cardId].img)
    if(cardChosen.length === 2){setTimeout(checkMatch,500)}
}
