document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll("form[data-validate]");

  const setFieldState = (input, isValid, message = "") => {
    const errorElement = document.getElementById(`${input.name}-error`);

    input.classList.remove("invalid", "valid");

    if (message) {
      input.classList.add("invalid");
      input.setAttribute("aria-invalid", "true");
      if (errorElement) {
        errorElement.textContent = message;
      }
      return false;
    }

    input.classList.add("valid");
    input.setAttribute("aria-invalid", "false");
    if (errorElement) {
      errorElement.textContent = "";
    }
    return true;
  };

  const validateField = (input) => {
    const value = input.value.trim();

    if (input.name === "name") {
      if (!value) {
        return setFieldState(input, false, "Informe seu nome.");
      }

      if (value.length < 2) {
        return setFieldState(
          input,
          false,
          "O nome deve ter pelo menos 2 caracteres.",
        );
      }

      return setFieldState(input, true);
    }

    if (input.name === "email") {
      if (!value) {
        return setFieldState(input, false, "Informe seu e-mail.");
      }

      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(value)) {
        return setFieldState(input, false, "Digite um e-mail válido.");
      }

      return setFieldState(input, true);
    }

    if (input.name === "password") {
      if (!value) {
        return setFieldState(input, false, "Informe sua senha.");
      }

      if (value.length < 8) {
        return setFieldState(
          input,
          false,
          "A senha deve ter pelo menos 8 caracteres.",
        );
      }

      return setFieldState(input, true);
    }

    return setFieldState(input, true);
  };

  forms.forEach((form) => {
    const fields = form.querySelectorAll("input");

    fields.forEach((input) => {
      input.addEventListener("input", () => validateField(input));
      input.addEventListener("blur", () => validateField(input));
    });

    form.addEventListener("submit", (event) => {
      let isFormValid = true;

      fields.forEach((input) => {
        if (!validateField(input)) {
          isFormValid = false;
        }
      });

      if (!isFormValid) {
        event.preventDefault();
      }
    });
  });
});
