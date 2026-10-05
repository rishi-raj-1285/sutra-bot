const form = document.querySelector("#chat-form");
const input = document.querySelector("#message-input");
const languageSelect = document.querySelector("#language-select");
const messages = document.querySelector("#messages");
const sendButton = form.querySelector("button[type='submit']");
const errorMessage = document.querySelector("#error-message");

function addMessage(text, sender) {
  const article = document.createElement("article");
  article.className = `message ${sender}-message`;

  const avatar = document.createElement("span");
  avatar.className = `avatar ${sender}-avatar`;
  avatar.setAttribute("aria-hidden", "true");
  avatar.textContent = sender === "bot" ? "सू" : "YOU";

  const content = document.createElement("div");
  content.className = "message-content";
  const speaker = document.createElement("span");
  speaker.className = "speaker";
  speaker.textContent = sender === "bot" ? "SutraBot" : "You";
  const paragraph = document.createElement("p");
  paragraph.textContent = text;

  content.append(speaker, paragraph);
  article.append(avatar, content);
  messages.append(article);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage(text) {
  const message = text.trim();
  if (!message) return;

  errorMessage.hidden = true;
  addMessage(message, "user");
  input.value = "";
  sendButton.disabled = true;

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, language: languageSelect.value })
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.response || "The server could not process that message.");
    addMessage(data.response, "bot");
  } catch (error) {
    errorMessage.textContent = error.message || "Could not reach SutraBot. Check that the Flask server is running and try again.";
    errorMessage.hidden = false;
  } finally {
    sendButton.disabled = false;
    input.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendMessage(input.value);
});

document.querySelectorAll(".suggestion").forEach((button) => {
  button.addEventListener("click", () => sendMessage(button.dataset.message));
});
