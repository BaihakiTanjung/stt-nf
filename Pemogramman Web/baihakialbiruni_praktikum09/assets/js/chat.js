const message = document.getElementById('message');
const chatSection = document.getElementById('chat-section');

function sendMessage() {
    let div1 = document.createElement('div');
    div1.classList.add('w-full', 'flex', 'justify-start');

    let div2 = document.createElement('div');
    div2.classList.add("bg-gray-100", "rounded", "px-5", "py-2", "my-2", "text-gray-700", "relative")
    div2.style.maxWidth = "300px";

    let span1 = document.createElement('span');
    span1.classList.add("block")
    span1.innerHTML = message.value;

    let span2 = document.createElement('span');
    span2.classList.add("block", "text-xs", "text-right")
    span2.innerHTML = "12:00pm";

    div2.appendChild(span1);
    div2.appendChild(span2);
    div1.appendChild(div2);

    chatSection.appendChild(div1);
}