function timeFormat(secs) {
    return `${leadingZero(Math.floor(secs / 60))}:${leadingZero(Math.floor(secs % 60))}`;
}

function leadingZero(n) {
    return `${n < 10 ? "0" : ""}${n}`
}

function update() {
    n.innerText = index.toString();
    t.innerText = timeFormat((Date.now() - startTime) / 1000);
}

const n = document.getElementById('n');
const t = document.getElementById('t');

let index = 1;
let startTime = Date.now();
let x = setInterval(() => {
    update();
}, 1000);

document.body.addEventListener('keydown', (e) => {
    if (e.key === " ") {
        if (e.shiftKey) {
            if (index > 1) {
                index--;
            };
        } else {
            index++;
        };
        update();
    };
});