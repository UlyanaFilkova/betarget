<script setup>
import ResumeActions from "@/components/crmComponents/resumeComponents/ResumeActions.vue";
import ResumeContent from "@/components/crmComponents/resumeComponents/ResumeContent.vue";
import ResumeInfo from "@/components/crmComponents/resumeComponents/ResumeInfo.vue";
</script>

<template>
  <div class="resume">
    <section class="resume-display">
      <ResumeActions />
      <ResumeContent />
    </section>
    <ResumeInfo />

    <div class="resume__not-chosen">Выберите резюме</div>
  </div>
</template>
