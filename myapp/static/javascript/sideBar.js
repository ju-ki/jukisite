class SideBarController {
    constructor(name) {
        this.name = name
        this.elem = this._init();
    }
    _init() {
        return document.querySelector("#" + this.name);
    }
    mouseOver() {
        this.elem.addEventListener("mouseover", function () {
            this.elem.style.color = "black";
            this.elem.style.backgroundColor = "white";
        }.bind(this), false);
    }
    mouseOut() {
        this.elem.addEventListener("mouseout", function () {
            this.elem.style.color = "";
            this.elem.style.backgroundColor = "";
        }.bind(this), false);
    }
    //ゴリ押し実装でとりあえず遷移するようにしている.これよりいいやり方があれば修正
    click() {
        this.elem.addEventListener("click", function () {
            location.href = "https://jukisite.herokuapp.com/" + this.name;
        }.bind(this), false);
    }
}
document.addEventListener("DOMContentLoaded", function () {
    const sideEvent1 = new SideBarController("introduction");
    const sideEvent2 = new SideBarController("skill");
    const sideEvent3 = new SideBarController("experience");
    const sideEvent4 = new SideBarController("works");
    const sideEvent5 = new SideBarController("blog");
    const sideEvent6 = new SideBarController("contact");
    const sideEvent7 = new SideBarController("news");
    setTimeout(() => {
        sideEvent1.mouseOver();
        sideEvent1.mouseOut();
        sideEvent1.click();
        sideEvent2.mouseOver();
        sideEvent2.mouseOut();
        sideEvent2.click();
        sideEvent3.mouseOver();
        sideEvent3.mouseOut();
        sideEvent3.click();
        sideEvent4.mouseOver();
        sideEvent4.mouseOut();
        sideEvent4.click();
        sideEvent5.mouseOver();
        sideEvent5.mouseOut();
        sideEvent5.click();
        sideEvent6.mouseOver();
        sideEvent6.mouseOut();
        sideEvent6.click();
        sideEvent7.mouseOver();
        sideEvent7.mouseOut();
        sideEvent7.click();
    }, 1000);
});