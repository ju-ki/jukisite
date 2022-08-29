class ButtonController {
    constructor(name) {
        this.name = name
        this.elem = this._init();
        this.nameDic = {
            "自己紹介": "introduction",
            "スキル": "skill",
            "ブログ": "blog",
            "今までやってきたこと": "experience",
            "連絡先": "contact"
        }
    }
    _init() {
        return document.querySelector("#" + this.name);
    }
    click() {
        this.name = this.nameDic[this.name];
        this.elem.addEventListener("click", function () {
            location.href = "https://jukisite.herokuapp.com/" + this.name;
        }.bind(this), false);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const buttonEvent1 = new ButtonController("自己紹介");
    const buttonEvent2 = new ButtonController("スキル");
    const buttonEvent3 = new ButtonController("ブログ");
    const buttonEvent4 = new ButtonController("今までやってきたこと");
    const buttonEvent5 = new ButtonController("連絡先");
    setTimeout(() => {
        buttonEvent1.click();
        buttonEvent2.click();
        buttonEvent3.click();
        buttonEvent4.click();
        buttonEvent5.click();
    }, 1000);
});