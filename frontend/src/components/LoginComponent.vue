<script setup>
import "@/assets/css/login.css";
import { reactive, ref, onMounted, computed } from "vue";
import router from "@/router";
import { RouterLink } from "vue-router";
import axios from "axios";

const form = reactive({
  email: "",
  password: "",
});

const loginEmail = ref(null);
const loginPassword = ref(null);

const errors = reactive({
  email: "",
  password: "",
  emptyFields: "",
});

const validatePassword = (password) => {
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
  return passwordRegex.test(password);
};

const checkEmail = () => {
  if (loginEmail.value.validity.typeMismatch) {
    errors.email = "Введите корректный email";
    return false;
  } else {
    errors.email = "";
    return true;
  }
};

const checkPassword = () => {
  if (!validatePassword(loginPassword.value.value)) {
    errors.password =
      "Пароль должен содержать не менее 8 символов и включать большие буквы и цифры";
    return false;
  } else {
    errors.password = "";
    return true;
  }
};

onMounted(() => {
  loginEmail.value.addEventListener("focusout", (event) => {
    if (checkEmail() === false) {
      loginEmail.value.addEventListener("input", checkEmail);
    } else {
      errors.email = "";
    }
  });

  loginPassword.value.addEventListener("focusout", (event) => {
    if (checkPassword() === false) {
      loginPassword.value.addEventListener("input", checkPassword);
    } else {
      errors.password = "";
    }
  });
});

const checkForm = () => {
  // заполнены ли все поля
  if (loginPassword.value.value === "" || loginEmail.value.value === "") {
    errors.emptyFields = "Заполните, пожалуйста, все поля";
    return false;
  } else {
    errors.emptyFields = "";
  }
  // если еще висят ошибки
  if (errors.email !== "" || errors.password !== "" || errors.emptyFields) {
    return false;
  }

  if (checkEmail() === false || checkPassword() === false) {
    return false;
  }

  return true;
};

const handleSubmit = async () => {
  if (!checkForm()) {
    return;
  }
  const userData = {
    username: form.email,
    password: form.password,
  };

  const params = new URLSearchParams(userData);

  try {
    const response = await axios.post("/api/login", params, {
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    });
  } catch (error) {
    console.error("Error login", error);
  }
};
</script>

<template>
  <section class="login">
    <div class="login__wrapper">
      <h1 class="login__logo">Betarget</h1>
      <form novalidate class="login__form" @submit.prevent="handleSubmit">
        <span
          :style="{ visibility: errors.emptyFields ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.emptyFields }}</span
        >
        <input
          class="login__input"
          type="email"
          id="login__email"
          name="login__email"
          v-model="form.email"
          placeholder="Электронная почта"
          autocomplete="email"
          ref="loginEmail"
          required
        />
        <span
          :style="{ visibility: errors.email ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.email }}</span
        >
        <input
          class="login__input"
          type="password"
          id="login__password"
          name="login__password"
          v-model="form.password"
          placeholder="Пароль"
          autocomplete="current-password"
          ref="loginPassword"
          required
        />
        <span
          :style="{ visibility: errors.password ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.password }}</span
        >
        <button class="login__button" type="submit">Вход</button>
      </form>
      <div class="login__links">
        <RouterLink to="" class="login__link">Забыли пароль? </RouterLink>
        <RouterLink to="/registration" class="login__link"
          >Создать аккаунт</RouterLink
        >
      </div>
    </div>
  </section>
</template>
