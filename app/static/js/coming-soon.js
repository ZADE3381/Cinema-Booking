const text = document.querySelector(".text");
const strText = text.textContent;
const splitText = strText.split("");

const onClick = () => {
  for (let i = 0; i < splitText.length; i++) {
    splitText[i].classList.remove("fade");

    let char = 0;

    let timer = setInterval(onTick, 70);

    console.log("click");
  }
};

text.textContent = "";

const complete = () => {
  clearInterval(timer);
  timer = null;
};

const onTick = () => {
  const span = text.querySelectorAll("span")[char];
  span.classList.add("fade");
  char++;
  if (char === splitText.length) {
    complete();
    return;
  }
};

for (let i = 0; i < splitText.length; i++) {
  text.innerHTML += `<span>${splitText[i]}</span>`;
}

let char = 0;

let timer = setInterval(onTick, 50);
