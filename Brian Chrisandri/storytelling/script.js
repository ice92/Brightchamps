setTimeout(() => {init();}, 10);
var page = 0;
var pages = ["Once upon a time, a man is walking through a pavement of a city. He loves looking at what happened with the city.",
"Suddenly, he fell to the drain that is very narrow, but also quite deep. He is stuck on the drain and can\'t go up. He is very scared being inside a drain.",
"“Help! Help!” said by the man, but no one responds to him. A few hours later, a woman found a man shouting from the drain. She is very panic when she found a man at the drain.",
"The woman will try finding tools at the supermarket and found a rope. She bought a rope and tries to help the man who have fell off the drain. Sadly, this method does not work.",
"She tried to call emergency, but the phone has run out of battery and can\'t call the emergency. She becomes more panic, and the man is trying to keep holding.",
"She found someone\'s phone and the woman said “May I borrow your phone?” to that person. The person says “yes” and she borrows the phone.",
"She tried to call emergency with that phone, but it suddenly run out of battery. She becomes very panic and wants to save the man who fell off to the drain.",
"She asked someone else to call emergency to save the man. The emergency call has started. The woman has started communicating with the emergency, saying that she was panic and wants to save the man.",
"Several minutes later, someone comes to the drain. He is trying to rescue the man that fell off from the drain, using a long rope. Someone else is also trying to help him.",
"Twenty minutes later, the man who fell off the drain finally get up and go out of the drain. The woman becomes excited because the man has been saved.",
"Several hours later, the man and the woman are now friends, and they became best friends forever. The end."];

function prevpage(event) {
    if (page > 0) {
        --page;
        update();
    };
}

function nextpage(event) {
    if (page < pages.length - 1) {
        ++page;
        update();
    };
}

function init() {
    document.getElementById('prev').addEventListener('click', ()=>{prevpage();});
    document.getElementById('next').addEventListener('click', ()=>{nextpage();});
    update();
}

function update() {
    document.getElementById('story').textContent = pages[page];
    document.getElementById('pagenumber').textContent = page + 1;
}