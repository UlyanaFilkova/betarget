<script setup>
import "@/assets/css/default.css";
import "@/assets/css/crm.css";
import Header from "@/components/crmComponents/Header.vue";
import Vacancies from "@/components/crmComponents/Vacancies.vue";
import Filters from "@/components/crmComponents/Filters.vue";
import ResumeList from "@/components/crmComponents/ResumeList.vue";
import Resume from "@/components/crmComponents/resumeComponents/Resume.vue";
</script>

<template>
  <Header />
  <div class="wrapper">
    <Vacancies />
    <Filters />
    <ResumeList />
    <Resume />
  </div>
</template>
