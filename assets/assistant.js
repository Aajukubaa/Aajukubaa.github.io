(function () {
    "use strict";

    const dataElement = document.getElementById("assistant-data");
    const assistant = dataElement ? JSON.parse(dataElement.textContent) : {};
    const launcher = document.getElementById("assistant-launcher");
    const panel = document.getElementById("assistant-panel");
    const closeButton = document.getElementById("assistant-close");
    const messages = document.getElementById("assistant-messages");
    const form = document.getElementById("assistant-form");
    const input = document.getElementById("assistant-input");
    const suggestionGroup = document.querySelector(".assistant-suggestions");
    const searchAssistantButton = document.getElementById("search-assistant-cta");

    function scrollMessagesToBottom() {
        if (messages) messages.scrollTop = messages.scrollHeight;
    }

    function appendMessage(text, sender) {
        const message = document.createElement("div");
        message.className = "assistant-message assistant-message-" + sender;
        message.textContent = text;
        messages.appendChild(message);
        scrollMessagesToBottom();
        return message;
    }

    function submitQuestion(question) {
        const value = String(question || "").trim();
        if (!value || !messages) return false;
        appendMessage(value, "user");
        if (input) input.value = "";

        const typing = document.createElement("div");
        typing.className = "assistant-message assistant-message-assistant assistant-typing";
        typing.setAttribute("role", "status");
        typing.setAttribute("aria-label", assistant.typing_label);
        for (let index = 0; index < 3; index += 1) {
            typing.appendChild(document.createElement("span"));
        }
        messages.appendChild(typing);
        scrollMessagesToBottom();

        window.setTimeout(() => {
            typing.remove();
            appendMessage(assistant.placeholder_reply, "assistant");
        }, 700);
        return true;
    }

    function openAssistant() {
        if (!panel) return false;
        panel.classList.add("assistant-open");
        panel.setAttribute("aria-hidden", "false");
        document.body.classList.add("assistant-open");
        window.setTimeout(() => input?.focus(), 100);
        return true;
    }

    function closeAssistant() {
        if (!panel?.classList.contains("assistant-open")) return false;
        panel.classList.remove("assistant-open");
        panel.setAttribute("aria-hidden", "true");
        document.body.classList.remove("assistant-open");
        window.requestAnimationFrame(() => launcher?.focus());
        return true;
    }

    window.openAssistant = openAssistant;
    window.closeAssistant = closeAssistant;

    launcher?.addEventListener("click", openAssistant);
    closeButton?.addEventListener("click", closeAssistant);
    searchAssistantButton?.addEventListener("click", () => window.openAssistant());

    form?.addEventListener("submit", (event) => {
        event.preventDefault();
        submitQuestion(input?.value);
    });

    suggestionGroup?.addEventListener("click", (event) => {
        const button = event.target.closest("[data-assistant-suggestion]");
        if (!button) return;
        submitQuestion(button.dataset.assistantSuggestion);
        input?.focus();
    });
})();
