async function load_messages() {

  const button = document.querySelector(".js-button");
  const url = button.getAttribute('data-url');
  const message_list = document.querySelector(".js-message-list");

  if (button.innerText === "Load messages") {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const messages = await response.json();

      messages.forEach(
        message => {
          const li = document.createElement("li");
          li.classList.add('list-group-item');
          li.textContent = `${message.id} - ${message.message}`;
          message_list.appendChild(li);
        }
      )
    } catch (error) {
      console.error(error);
    }
    button.innerText = "Hide messages";
  } else {
    message_list.innerHTML = "";
    button.innerText = "Load messages";
  }
}
