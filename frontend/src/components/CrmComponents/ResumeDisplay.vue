<template>
  <section class="resume-display">
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
    <div class="resume-content">
      <div class="resume-content__skills">
        <h3>Ключевые навыки</h3>
        <ul class="resume-content__skills-list">
          <li>Python</li>
          <li>Django</li>
          <li>Flask</li>
          <li>SQL</li>
          <li>NoSQL</li>
          <li>RESTful API</li>
          <li>Тестирование кода</li>
          <li>Оптимизация производительности</li>
        </ul>
      </div>
      <div class="resume-content__experience">
        <h3>Опыт работы</h3>
        <p>
          Я работал в качестве Python-разработчика в компании XYZ с 2018 года. В
          мои обязанности входило разработка и поддержка веб-приложений на
          основе фреймворка Django, создание и оптимизация баз данных, а также
          взаимодействие с другими членами команды разработки для достижения
          поставленных целей проекта.
        </p>
      </div>
      <div class="resume-content__education">
        <h3>Образование</h3>
        <p>
          Я получил степень бакалавра в области компьютерных наук в университете
          ABC. Во время учебы я изучал различные аспекты программирования,
          алгоритмы и структуры данных. Моя специализация была связана с
          разработкой программного обеспечения, и я активно участвовал в
          проектах, где использовался язык Python.
        </p>
      </div>
      <div class="resume-content__about">
        <h3>О себе</h3>
        <p>
          Python-разработчик с фокусом на веб-разработке. Имею глубокие знания
          языка Python, фреймворков Django и Flask, а также опыт работы с базами
          данных SQL и NoSQL. Мои навыки также включают разработку RESTful API,
          тестирование кода и оптимизацию производительности.
        </p>
      </div>
    </div>
  </section>
</template>
