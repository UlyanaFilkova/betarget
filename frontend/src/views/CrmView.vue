<script setup>
import "@/assets/css/default.css";
import "@/assets/css/crm.css";
import Header from "@/components/CrmComponents/Header.vue";
import Vacancies from "@/components/CrmComponents/Vacancies.vue";
import Filters from "@/components/CrmComponents/Filters.vue";
import ResumeList from "@/components/CrmComponents/ResumeList.vue";
import Resume from "@/components/CrmComponents/Resume.vue";
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
