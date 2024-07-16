<template>
  <div class="resume-display__actions">
    <div class="resume-display__stage">
      <p class="resume-display__current-stage" data-stage=""></p>
      <button class="resume-display__change-stage">Сменить этап</button>
      <!-- <p>Выберите этап</p> -->
      <select class="resume-display__stage-input">
        <option value="in_work">В работе</option>
        <option value="screening">Скрининг</option>
        <option value="interview">Интервью</option>
        <option value="offer">Оффер</option>
        <option value="rejected">Отказ</option>
      </select>
      <div class="resume-display__stage-actions">
        <button class="resume-display__save-stage" disabled>Сохранить</button>
        <button class="resume-display__cancel-stage">Отмена</button>
      </div>
    </div>
    <div class="resume-display__history"></div>
  </div>
</template>
