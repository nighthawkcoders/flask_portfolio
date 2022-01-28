// Beanie Toggle Function
beanienumber=0;
function BeanieToggle() {
    const images = ["/static/rohanblackbeanie.jpg",
        "/static/rohanbrownbeanie.jpg"
    ];
    if (beanienumber == 0) {
        document.getElementById("beanie").src = images[0]
        beanienumber = 1;
    } else if (beanienumber == 1) {
        document.getElementById("beanie").src = images[1]
        beanienumber = 0;
    }
}

// Lucky Number Function with 22
function LuckyNumber() {
    let value1 = parseInt(document.getElementById('value1').value);
    if (value1 === 22) {
        document.getElementById('result').innerHTML = "Well Done!"
    }
    else if (value1 > 22 ) {
        document.getElementById('result').innerHTML = "Too High!"
    }
    else if (value1 < 22) {
        document.getElementById('result').innerHTML = "Too Low!"
    }
}

// Show and Hide Function
function ShowAndHide() {
    var x = document.getElementById('SectionName');
    if (x.style.display == 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}

