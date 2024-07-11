<script setup></script>

<template>
  <section class="login">
    <h1 class="logo">Betarget</h1>
    <form>
      <input
        type="email"
        id="login__email"
        name="login__email"
        placeholder="Электронная почта"
        required
      />

      <input
        type="password"
        id="login__password"
        name="login__password"
        placeholder="Пароль"
        required
      />

      <button type="submit">Вход</button>
    </form>
    <p>
      <a href="#">Забыли пароль?</a>
      <a href="#">Создать аккаунт</a>
    </p>
  </section>
</template>
