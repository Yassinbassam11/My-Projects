cardArray = [
    {
        name:'cheeseburger',
        img:'images/cheeseburger.png'
    },
    {
        name:'fries',
        img:'images/fries.png'
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
        name:'cheeseburger',
        img:'images/cheeseburger.png'
    },
    {
        name:'fries',
        img:'images/fries.png'
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

cardArray.sort(() => 0.5 - Math.random())
let chosenCards = []
let chosenCardsId = []
let cardsWon = []
const boardDisplay = document.querySelector('#board')
const resultDisplay = document.querySelector('#result')
const resetButton = document.querySelector('#reset-button')

function createBoard(){
    for(let i=0;i<cardArray.length;i++){
        const card = document.createElement('img')
        card.setAttribute('src','images/blank.png')
        card.setAttribute('data-id',i)
        card.addEventListener('click',flipCard)
        boardDisplay.append(card)
    }
    resultDisplay.innerHTML='0'
    resetButton.addEventListener('click',reset)
}
createBoard()

function flipCard(){
    const cardId = this.getAttribute('data-id')
    this.setAttribute('src',cardArray[cardId].img)
    chosenCards.push(cardArray[cardId])
    chosenCardsId.push(cardId)
    if(chosenCards.length==2){setTimeout(checkMatch,500)}
    console.log(chosenCards)
    console.log(chosenCardsId)
}

function checkMatch(){
    const cards = document.querySelectorAll('#board img')
    console.log(cards)
    console.log("check for match!")
    if(chosenCardsId[0]==chosenCardsId[1]){
        alert('You choose the same card twice!')
        cards[chosenCardsId[0]].setAttribute('src','images/blank.png')
    }
    else if(chosenCards[0].name == chosenCards[1].name){
        cards[chosenCardsId[0]].setAttribute('src','images/white.png')
        cards[chosenCardsId[1]].setAttribute('src','images/white.png')
        cardsWon.push(chosenCards[0])
        cardsWon.push(chosenCards[1])
        cards[chosenCardsId[0]].removeEventListener('click',flipCard)
        cards[chosenCardsId[1]].removeEventListener('click',flipCard)
        resultDisplay.innerHTML = (cardsWon.length/2)
    }
    else{
        cards[chosenCardsId[0]].setAttribute('src','images/blank.png')
        cards[chosenCardsId[1]].setAttribute('src','images/blank.png')
    }
    chosenCards = []
    chosenCardsId = []
    console.log(cardsWon)
}

function reset(){
    cardArray.sort(() => 0.5 - Math.random())
    // const cards = document.querySelectorAll('#board img')
    // for(let i=0;i<cards.length;i++){
    //     cards[i].setAttribute('src','images/blank.png')
    // }
    let temp = document.querySelectorAll('#board img')
    for(let i=0;i<temp.length;i++){
        temp[i].remove()
    }
    createBoard()
}
