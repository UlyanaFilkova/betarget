<template>
  <section class="resume-info">
    <div class="resume__info-container">
      <div class="resume-info__rating-result">
        <p>Оценка:</p>
        <span id="resume-info__rating" class="resume-info__rating-result-span"
          >0</span
        >
        / 10
      </div>
      <div class="resume-info__rating-slider">
        <button
          class="resume-info__arrow resume-info__arrow_minus"
          id="resume-info__decrease"
        >
          -
        </button>
        <input
          type="range"
          id="resume-info__slider"
          min="0"
          max="10"
          value="0"
          class="resume-info__slider"
        />
        <button
          class="resume-info__arrow resume-info__arrow_plus"
          id="resume-info__increase"
        >
          +
        </button>
      </div>
      <div class="resume-info__photo-container">
        <div class="resume-info__photo-wrapper">
          <img
            src="../static/img/default_profile_photo.jpg"
            class="resume-info__photo"
          />
        </div>
      </div>
      <div class="resume-info__name">Александр Ильин</div>
      <div class="resume-info__position">Unity Gamedev</div>
      <div class="resume-info__list">
        <li>
          <h6>Телефон</h6>
          <div class="resume-info__list-component">
            <a
              href="tel:+89036251683"
              type="tel"
              class="resume-info__phone"
            ></a>
          </div>
        </li>
        <li>
          <h6>Email</h6>
          <div class="resume-info__list-component">
            <a
              href="mailto:sakutin@gmail.com"
              type="email"
              class="resume-info__email"
            ></a>
            <!-- <p class="resume-info__email"></p> -->
          </div>
        </li>
        <li>
          <h6>Город</h6>
          <div class="resume-info__list-component resume-info__city">
            Москва
          </div>
        </li>
        <li>
          <h6>Желаемая ЗП</h6>
          <div class="resume-info__list-component resume-info__salary">
            $2000
          </div>
        </li>
        <li>
          <h6>Возраст</h6>
          <div class="resume-info__list-component resume-info__age">26</div>
        </li>
      </div>
      <div class="resume-info__contacts"></div>
    </div>
  </section>
</template>
