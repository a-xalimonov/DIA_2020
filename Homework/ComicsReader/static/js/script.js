function tableSearch() {

    let phrase = document.getElementsByClassName('search-text')[0];
    let table = document.getElementsByClassName('table')[0];
    let regPhrase = new RegExp(phrase.value, 'i');
    let flag;
    for (let i = 1; i < table.rows.length; i++) {
        flag = false;
        for (let j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }
    }
}

function sizeChange() {
    let size = document.getElementsByClassName('size-option')[0];
    let scale;
    switch(size.value) {
        case '50%':
            scale = 0.5
            break;
        case '75%':
            scale = 0.75
            break;
        case '100%':
            scale = 1;
            break;
        case '150%':
            scale = 1.5
            break;
        case '200%':
            scale = 2;
            break;
    }
    let pages = document.getElementsByClassName('comic-page');

    for (let i = 0; i < pages.length; i++) {
        pages[i].width = pages[i].naturalWidth * scale
    }
}